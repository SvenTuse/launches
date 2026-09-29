import { test } from 'node:test';
import assert from 'node:assert/strict';
import { promises as fs } from 'node:fs';
import path from 'node:path';
import { safeRelative, readFile, writeFile, revision, catalog, StorageError, writable } from '../lib/storage';
import { relativeLink, overviewInfo } from '../lib/content';

test('paths cannot escape the case study or expose hidden and system files', () => {
  for (const value of ['../.env.local', 'x/../../secret', '/etc/passwd', 'C:/Windows', 'x\\y', '.env.local', 'foo/.secret', 'CON.txt', 'x//y', 'file.']) assert.throws(() => safeRelative(value), StorageError);
  assert.equal(safeRelative('Новая папка/Мой отчёт.md'), 'Новая папка/Мой отчёт.md');
});
test('Markdown links resolve in root and nested folders, including spaces', () => {
  assert.equal(relativeLink('X-Flow.md', 'x-posts/Screenshot_1.jpg'), 'x-posts/Screenshot_1.jpg');
  assert.equal(relativeLink('notes/analysis.md', '../x-posts/Мой%20скрин.png'), 'x-posts/Мой скрин.png');
});
test('project metadata accepts plain and formatted overview files', () => {
  const plain = overviewInfo('Name:Crumbs\nTicker:CRUMBS\nX:https://x.com/crumbsfamily');
  assert.equal(plain.Name, 'Crumbs'); assert.equal(plain.X, 'https://x.com/crumbsfamily');
  const formatted = overviewInfo('- **Name:** Deed Estate.\n- **Ticker:** DEED.\n- **Website:** [deed.estate](https://deed.estate/).\n- **ATH capitalization:** **$4.28M — reported** in the original overview');
  assert.equal(formatted.Ticker, 'DEED'); assert.equal(formatted.Website, 'https://deed.estate/'); assert.equal(formatted.ATH, '$4.28M');
});

test('a connected Vercel Blob store is writable with OIDC credentials', () => {
  const names = ['STORAGE_DRIVER', 'BLOB_READ_WRITE_TOKEN', 'BLOB_STORE_ID', 'VERCEL_OIDC_TOKEN'] as const;
  const original = Object.fromEntries(names.map(name => [name, process.env[name]]));
  try {
    process.env.STORAGE_DRIVER = 'blob';
    delete process.env.BLOB_READ_WRITE_TOKEN;
    delete process.env.BLOB_STORE_ID;
    delete process.env.VERCEL_OIDC_TOKEN;
    assert.equal(writable(), false);
    process.env.BLOB_STORE_ID = 'store_test';
    process.env.VERCEL_OIDC_TOKEN = 'oidc_test';
    assert.equal(writable(), true);
  } finally {
    for (const name of names) {
      if (original[name] === undefined) delete process.env[name];
      else process.env[name] = original[name];
    }
  }
});
test('local writes persist, reject duplicates and concurrent stale changes, and back up originals', async () => {
  process.env.STORAGE_DRIVER = 'local'; delete process.env.VERCEL;
  const id = 'test-storage-' + Date.now();
  const directory = path.resolve('case-study projects', id);
  await fs.mkdir(directory);
  try {
    const first = Buffer.from('# First');
    const rev = await writeFile(id, 'notes/test.md', first, null, true);
    assert.deepEqual(await readFile(id, 'notes/test.md'), first);
    await assert.rejects(writeFile(id, 'notes/test.md', first, null, true), (e: unknown) => e instanceof StorageError && e.status === 409);
    const updates = await Promise.allSettled([writeFile(id, 'notes/test.md', Buffer.from('# A'), rev, false), writeFile(id, 'notes/test.md', Buffer.from('# B'), rev, false)]);
    assert.equal(updates.filter(r => r.status === 'fulfilled').length, 1);
    assert.equal(updates.filter(r => r.status === 'rejected').length, 1);
    assert.equal(revision(await readFile(id, 'notes/test.md')), revision(Buffer.from('# A')));
    const backupDir = path.resolve('.local-history', id, encodeURIComponent('notes/test.md'));
    const backups = await fs.readdir(backupDir);
    assert.equal(backups.length, 1); assert.deepEqual(await fs.readFile(path.join(backupDir, backups[0])), first);
    await assert.rejects(readFile(id, '../../.env.local'), StorageError);
    const library = await catalog();
    assert.ok(library.projects.find(p => p.id === id)?.files.some(f => f.path === 'notes/test.md'));
  } finally {
    // Both targets are unique directories created by this test, below the workspace.
    assert.equal(path.dirname(directory), path.resolve('case-study projects'));
    await fs.rm(directory, { recursive: true, force: true });
    const history = path.resolve('.local-history', id);
    assert.equal(path.dirname(history), path.resolve('.local-history'));
    await fs.rm(history, { recursive: true, force: true });
  }
});
