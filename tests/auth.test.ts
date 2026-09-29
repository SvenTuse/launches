import { test } from 'node:test';
import assert from 'node:assert/strict';
import { sameOrigin, equalSecret, createSession } from '../lib/auth';
import { jwtVerify } from 'jose';

test('same-origin validation works behind Next proxy and rejects unrelated sites', () => {
  assert.equal(sameOrigin(new Request('http://0.0.0.0:3000/api/auth', { headers: { host: 'localhost:3000', origin: 'http://localhost:3000' } })), true);
  assert.equal(sameOrigin(new Request('https://app.example/api/file', { headers: { host: 'app.example', origin: 'https://evil.example' } })), false);
  assert.equal(sameOrigin(new Request('https://app.example/api/file', { headers: { host: 'app.example' } })), false);
  assert.equal(sameOrigin(new Request('https://app.example/api/file', { headers: { host: 'app.example', origin: 'null' } })), false);
});
test('credentials compare exactly and sessions have a signed 12-hour expiry', async () => {
  assert.equal(equalSecret('secret', 'secret'), true); assert.equal(equalSecret('secret', 'secret '), false);
  process.env.SESSION_SECRET = 'unit-test-secret-32-characters-long'; process.env.ADMIN_USERNAME = 'admin';
  const token = await createSession(); const key = new TextEncoder().encode(process.env.SESSION_SECRET);
  const { payload } = await jwtVerify(token, key);
  assert.equal(payload.sub, 'admin'); assert.equal(payload.role, 'admin'); assert.equal(payload.exp! - payload.iat!, 43200);
  const [header, , signature] = token.split('.');
  const forged = `${header}.${Buffer.from(JSON.stringify({ role: 'admin', sub: 'other' })).toString('base64url')}.${signature}`;
  await assert.rejects(jwtVerify(forged, key));
});
