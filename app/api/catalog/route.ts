import { authenticated } from '@/lib/auth';
import { catalog } from '@/lib/storage';
export const dynamic = 'force-dynamic';
export async function GET() {
  if (!await authenticated()) return Response.json({ error: 'Please sign in' }, { status: 401 });
  try { return Response.json(await catalog(), { headers: { 'Cache-Control': 'private, no-store' } }); }
  catch (e) { console.error('Catalog read failed', e); return Response.json({ error: 'Could not load the library. Check the storage connection.' }, { status: 503 }); }
}
