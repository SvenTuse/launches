import { SignJWT, jwtVerify } from 'jose';
import { cookies } from 'next/headers';
import { createHash, timingSafeEqual } from 'node:crypto';

export const COOKIE = 'kai_session';
function secret() {
  const value = process.env.SESSION_SECRET;
  if (!value || value.length < 32) throw new Error('Set SESSION_SECRET (32+ characters)');
  return new TextEncoder().encode(value);
}
export function equalSecret(a: string, b: string) {
  return timingSafeEqual(createHash('sha256').update(a).digest(), createHash('sha256').update(b).digest());
}
export async function createSession() {
  return new SignJWT({ role: 'admin' }).setProtectedHeader({ alg: 'HS256' }).setSubject(process.env.ADMIN_USERNAME || 'admin').setIssuedAt().setExpirationTime('12h').sign(secret());
}
export async function authenticated() {
  const token = (await cookies()).get(COOKIE)?.value;
  if (!token) return false;
  try { const { payload } = await jwtVerify(token, secret(), { algorithms: ['HS256'] }); return payload.role === 'admin' && payload.sub === (process.env.ADMIN_USERNAME || 'admin'); } catch { return false; }
}
export function sameOrigin(request: Request) {
  const origin = request.headers.get('origin');
  if (!origin) return false;
  try {
    const url = new URL(origin);
    // Next's internal request URL can use 0.0.0.0 behind a proxy/dev server.
    // Browser-controlled Origin must match the actual incoming Host header.
    return /^https?:$/.test(url.protocol) && url.host === request.headers.get('host');
  } catch { return false; }
}
