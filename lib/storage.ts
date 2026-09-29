import { promises as fs } from 'node:fs';
import path from 'node:path';
import { createHash, randomUUID } from 'node:crypto';
import { get, list, put } from '@vercel/blob';
import { fileKind, type FileEntry, type Project, type Catalog } from './types';
import { overviewInfo } from './content';

const ROOT = process.cwd();
const CASES = path.join(ROOT, 'case-study projects');
const PREFIX = 'kai-library/';
export const MAX_UPLOAD = 4 * 1024 * 1024;
export const driver = () => process.env.STORAGE_DRIVER === 'blob' || !!process.env.VERCEL ? 'blob' : 'local';
export const writable = () => driver() === 'local' || !!process.env.BLOB_READ_WRITE_TOKEN;
export class StorageError extends Error { constructor(message: string, public status = 400) { super(message); } }
export function safeRelative(value: string) {
  if (typeof value !== 'string' || !value || value.length > 500 || value.includes('\\') || /[\x00-\x1f<>:"|?*]/.test(value) || value.split('/').some(p => !p || p === '.' || p === '..' || p.startsWith('.') || /[. ]$/.test(p) || /^(con|prn|aux|nul|com[1-9]|lpt[1-9])(\.|$)/i.test(p))) throw new StorageError('Invalid path');
  return value;
}
export async function projectRoot(id: string) {
  safeRelative(id);
  if (id.includes('/')) throw new StorageError('Project not found', 404);
  const resolved = id === '_guide' ? path.join(ROOT, 'how we do it') : path.join(CASES, id);
  const stat = await fs.lstat(resolved).catch(() => null);
  if (!stat?.isDirectory() || stat.isSymbolicLink()) throw new StorageError('Project not found', 404);
  return resolved;
}
async function localPath(id: string, relative: string) {
  const root = await projectRoot(id);
  safeRelative(relative);
  const parts = relative.split('/');
  let cursor = root;
  for (const part of parts) {
    cursor = path.join(cursor, part);
    const stat = await fs.lstat(cursor).catch((e: NodeJS.ErrnoException) => { if (e.code !== 'ENOENT') throw e; return null; });
    if (stat?.isSymbolicLink()) throw new StorageError('Symbolic links are not supported');
  }
  return cursor;
}
const blobKey = (id: string, p: string) => `${PREFIX}${encodeURIComponent(id)}/${p.split('/').map(encodeURIComponent).join('/')}`;
export const revision = (buffer: Uint8Array) => createHash('sha256').update(buffer).digest('hex');
export async function readFile(id: string, relative: string): Promise<Buffer> {
  const local = await localPath(id, relative);
  if (driver() === 'blob' && process.env.BLOB_READ_WRITE_TOKEN) {
    const result = await get(blobKey(id, relative), { access: 'private', useCache: false });
    if (result?.statusCode === 200) return Buffer.from(await new Response(result.stream).arrayBuffer());
  }
  try { return await fs.readFile(local); } catch (e) { if ((e as NodeJS.ErrnoException).code === 'ENOENT') throw new StorageError('File not found', 404); throw e; }
}
async function scan(root: string, relative = ''): Promise<FileEntry[]> {
  const entries = await fs.readdir(path.join(root, relative), { withFileTypes: true });
  const nested = await Promise.all(entries.filter(e => !e.name.startsWith('.') && !e.isSymbolicLink()).map(async e => {
    const p = relative ? `${relative}/${e.name}` : e.name;
    if (e.isDirectory()) return scan(root, p);
    const stat = await fs.stat(path.join(root, p));
    return [{ path: p, size: stat.size, modified: stat.mtime.toISOString(), kind: fileKind(p) }];
  }));
  return nested.flat();
}
export async function catalog(): Promise<Catalog> {
  const folders = (await fs.readdir(CASES, { withFileTypes: true })).filter(e => e.isDirectory() && !e.isSymbolicLink() && !e.name.startsWith('.')).map(e => e.name);
  if (await fs.stat(path.join(ROOT, 'how we do it')).catch(() => null)) folders.push('_guide');
  const overlays = new Map<string, FileEntry[]>();
  if (driver() === 'blob' && process.env.BLOB_READ_WRITE_TOKEN) {
    let cursor: string | undefined;
    do {
      const result = await list({ prefix: PREFIX, cursor, limit: 1000 });
      for (const blob of result.blobs) {
        const [id, ...rest] = blob.pathname.slice(PREFIX.length).split('/').map(decodeURIComponent);
        const p = rest.join('/');
        overlays.set(id, [...(overlays.get(id) || []), { path: p, size: blob.size, modified: blob.uploadedAt.toISOString(), kind: fileKind(p) }]);
      }
      cursor = result.hasMore ? result.cursor : undefined;
    } while (cursor);
  }
  const projects = await Promise.all(folders.map(async id => {
    const localFiles = await scan(await projectRoot(id));
    const map = new Map(localFiles.map(f => [f.path, f]));
    for (const file of overlays.get(id) || []) map.set(file.path, file);
    const files = [...map.values()].sort((a, b) => a.path.localeCompare(b.path, undefined, { numeric: true }));
    let info: Record<string, string> = {};
    const infoFile = files.find(f => /^project[- ]info\.json$/i.test(f.path));
    if (infoFile) {
      try { const parsed = JSON.parse((await readFile(id, infoFile.path)).toString('utf8')); if (parsed && typeof parsed === 'object' && !Array.isArray(parsed)) for (const [key, value] of Object.entries(parsed)) if (typeof value === 'string' || typeof value === 'number') info[key] = String(value); } catch (e) { if (!(e instanceof SyntaxError)) throw e; }
    }
    if (!infoFile) {
      const overview = files.find(f => /^project[- ]overview\.md$/i.test(f.path));
      if (overview) info = overviewInfo((await readFile(id, overview.path)).toString('utf8'));
    }
    return { id, name: info.Name || (id === '_guide' ? 'Research playbook' : id.replace(/\(done\)/i, '').trim()), ticker: info.Ticker || '', status: id === '_guide' ? 'guide' : /template/i.test(id) ? 'template' : /\(done\)/i.test(id) ? 'complete' : 'research', info, files, cover: files.find(f => f.kind === 'image' && f.path.startsWith('x-posts/'))?.path || files.find(f => f.kind === 'image')?.path } as Project;
  }));
  return { projects, storage: driver(), writable: writable() };
}
// Serialize local edits to make revision checks and atomic writes one operation.
const locks = new Map<string, Promise<unknown>>();
export async function writeFile(id: string, relative: string, data: Buffer, expected: string | null, create: boolean) {
  const key = blobKey(id, relative);
  const prior = locks.get(key) || Promise.resolve();
  const work = prior.catch(() => {}).then(async () => {
    const target = await localPath(id, relative);
    if (!writable()) throw new StorageError('Connect a private Vercel Blob store to save files', 503);
    let existing: Buffer | null = null;
    try { existing = await readFile(id, relative); } catch (e) { if (!(e instanceof StorageError) || e.status !== 404) throw e; }
    if (create && existing) throw new StorageError('A file with this name already exists', 409);
    if (!create && (!existing || !expected || revision(existing) !== expected)) throw new StorageError('The file has changed. Open it again before saving.', 409);
    if (driver() === 'blob') {
      const current = await get(key, { access: 'private', useCache: false });
      // Check content against the ETag snapshot used in the conditional write.
      if (current?.statusCode === 200) {
        const bytes = Buffer.from(await new Response(current.stream).arrayBuffer());
        if (create || revision(bytes) !== expected) throw new StorageError('The file was changed in another tab', 409);
      }
      await put(key, data, { access: 'private', addRandomSuffix: false, allowOverwrite: !!current, ...(current ? { ifMatch: current.blob.etag } : {}), contentType: mime(relative) });
    } else {
      await fs.mkdir(path.dirname(target), { recursive: true });
      if (existing) {
        const history = path.join(ROOT, '.local-history', encodeURIComponent(id), encodeURIComponent(relative));
        await fs.mkdir(history, { recursive: true });
        await fs.writeFile(path.join(history, `${Date.now()}-${randomUUID()}.bak`), existing);
      }
      if (create) await fs.writeFile(target, data, { flag: 'wx' });
      else { const temp = `${target}.${randomUUID()}.tmp`; await fs.writeFile(temp, data); await fs.rename(temp, target); }
    }
    return revision(data);
  });
  locks.set(key, work);
  try { return await work; } finally { if (locks.get(key) === work) locks.delete(key); }
}
export function mime(p: string): string {
  const ext = p.split('.').pop()?.toLowerCase() || '';
  return ({ png: 'image/png', jpg: 'image/jpeg', jpeg: 'image/jpeg', webp: 'image/webp', gif: 'image/gif', avif: 'image/avif', mp4: 'video/mp4', webm: 'video/webm', mov: 'video/quicktime', mp3: 'audio/mpeg', wav: 'audio/wav', ogg: 'audio/ogg', m4a: 'audio/mp4', pdf: 'application/pdf', md: 'text/plain; charset=utf-8', txt: 'text/plain; charset=utf-8', json: 'application/json', csv: 'text/plain; charset=utf-8' } as Record<string, string>)[ext] || 'application/octet-stream';
}
