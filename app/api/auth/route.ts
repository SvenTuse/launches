import { NextResponse } from 'next/server';
import { COOKIE, createSession, equalSecret, sameOrigin } from '@/lib/auth';

const attempts = new Map<string, { count: number; until: number }>();
export async function POST(request: Request) {
  if (!sameOrigin(request)) return NextResponse.json({ error: 'Invalid request origin' }, { status: 403 });
  if (!process.env.ADMIN_PASSWORD || !process.env.SESSION_SECRET) return NextResponse.json({ error: 'Set ADMIN_PASSWORD and SESSION_SECRET on the server' }, { status: 503 });
  const ip = request.headers.get('x-forwarded-for')?.split(',')[0] || 'local';
  const now = Date.now();
  for (const [key, value] of attempts) if (value.until < now) attempts.delete(key);
  const attempt = attempts.get(ip) || { count: 0, until: now + 15 * 60_000 };
  if (attempt.count >= 10) return NextResponse.json({ error: 'Too many attempts. Try again in 15 minutes.' }, { status: 429 });
  if (Number(request.headers.get('content-length')) > 4096) return new Response(null, { status: 413 });
  const input = await request.json().catch(() => null);
  const body = input && typeof input === 'object' ? input : {};
  attempt.count++; attempts.set(ip, attempt);
  const username = typeof body.username === 'string' ? body.username : '';
  const password = typeof body.password === 'string' ? body.password : '';
  const nameOK = equalSecret(username, process.env.ADMIN_USERNAME || 'admin');
  const passOK = equalSecret(password, process.env.ADMIN_PASSWORD);
  if (!nameOK || !passOK) {
    await new Promise(resolve => setTimeout(resolve, 650));
    return NextResponse.json({ error: 'Incorrect username or password' }, { status: 401 });
  }
  attempts.delete(ip);
  const response = NextResponse.json({ ok: true });
  response.cookies.set(COOKIE, await createSession(), { httpOnly: true, secure: process.env.NODE_ENV === 'production', sameSite: 'strict', path: '/', maxAge: 12 * 60 * 60 });
  return response;
}
export async function DELETE(request: Request) {
  if (!sameOrigin(request)) return new Response(null, { status: 403 });
  const response = NextResponse.json({ ok: true }); response.cookies.delete(COOKIE); return response;
}
