import { authenticated, sameOrigin } from '@/lib/auth';
import { readFile, writeFile, revision, mime, StorageError, MAX_UPLOAD } from '@/lib/storage';
export const dynamic = 'force-dynamic';
export const runtime = 'nodejs';
function failure(e: unknown) {
  if (e instanceof StorageError) return Response.json({ error: e.message }, { status: e.status });
  if ((e as { statusCode?: number }).statusCode === 412 || /precondition|already exists/i.test(String(e))) return Response.json({ error: 'The file has changed or already exists. Open it again.' }, { status: 409 });
  console.error('File operation failed', e);
  return Response.json({ error: 'Could not complete the file operation' }, { status: 500 });
}
export async function GET(request: Request) {
  if (!await authenticated()) return Response.json({ error: 'Please sign in' }, { status: 401 });
  try {
    const params = new URL(request.url).searchParams;
    const p = params.get('path') || '';
    const bytes = await readFile(params.get('project') || '', p);
    const type = mime(p);
    const inline = /^(image|video|audio)\//.test(type) || type.startsWith('text/plain') || type === 'application/json';
    const headers: Record<string, string> = { 'Content-Type': type, 'Cache-Control': 'private, no-store', 'X-Revision': revision(bytes), 'Accept-Ranges': 'bytes', 'Content-Security-Policy': "default-src 'none'; sandbox", 'Content-Disposition': `${params.has('download') || !inline ? 'attachment' : 'inline'}; filename*=UTF-8''${encodeURIComponent(p.split('/').pop() || 'file')}` };
    const range = request.headers.get('range');
    if (range && /^(video|audio)\//.test(type)) {
      const match = range.match(/^bytes=(\d*)-(\d*)$/);
      if (!match) return new Response(null, { status: 416, headers: { 'Content-Range': `bytes */${bytes.length}` } });
      const start = match[1] ? Number(match[1]) : Math.max(0, bytes.length - Number(match[2]));
      const end = match[1] && match[2] ? Math.min(Number(match[2]), bytes.length - 1) : bytes.length - 1;
      if (start > end || start >= bytes.length) return new Response(null, { status: 416, headers: { 'Content-Range': `bytes */${bytes.length}` } });
      return new Response(new Uint8Array(bytes.subarray(start, end + 1)), { status: 206, headers: { ...headers, 'Content-Range': `bytes ${start}-${end}/${bytes.length}`, 'Content-Length': String(end - start + 1) } });
    }
    return new Response(new Uint8Array(bytes), { headers });
  } catch (e) { return failure(e); }
}
export async function PUT(request: Request) {
  if (!await authenticated()) return Response.json({ error: 'Please sign in' }, { status: 401 });
  if (!sameOrigin(request)) return new Response(null, { status: 403 });
  try {
    if (Number(request.headers.get('content-length')) > MAX_UPLOAD) throw new StorageError('Maximum 4 MB', 413);
    const body = await request.json();
    if (typeof body.content !== 'string' || typeof body.path !== 'string' || !/\.(md|txt|json|csv)$/i.test(body.path)) throw new StorageError('Only MD, TXT, JSON and CSV files can be edited');
    const bytes = Buffer.from(body.content, 'utf8');
    if (bytes.length > MAX_UPLOAD) throw new StorageError('Maximum 4 MB', 413);
    if (/\.json$/i.test(body.path)) try { JSON.parse(body.content); } catch { throw new StorageError('Invalid JSON. Fix the error before saving.'); }
    const rev = await writeFile(body.project, body.path, bytes, body.revision, body.create === true);
    return Response.json({ revision: rev });
  } catch (e) { return failure(e); }
}
export async function POST(request: Request) {
  if (!await authenticated()) return Response.json({ error: 'Please sign in' }, { status: 401 });
  if (!sameOrigin(request)) return new Response(null, { status: 403 });
  try {
    if (Number(request.headers.get('content-length')) > MAX_UPLOAD + 10000) throw new StorageError('Maximum 4 MB per file', 413);
    const form = await request.formData();
    const file = form.get('file');
    if (!(file instanceof File) || file.size > MAX_UPLOAD) throw new StorageError('Choose a file no larger than 4 MB', 413);
    const relative = String(form.get('path') || file.name);
    const allowed = /\.(md|txt|json|csv|png|jpe?g|webp|gif|avif|pdf|mp4|webm|mov|mp3|wav|ogg|m4a|zip)$/i;
    if (!allowed.test(relative)) throw new StorageError('Unsupported format. Choose a document, image, audio, video or ZIP file.');
    const bytes = Buffer.from(await file.arrayBuffer());
    if (/\.json$/i.test(relative)) try { JSON.parse(bytes.toString('utf8')); } catch { throw new StorageError('The file contains invalid JSON'); }
    await writeFile(String(form.get('project') || ''), relative, bytes, null, true);
    return Response.json({ ok: true });
  } catch (e) { return failure(e); }
}
