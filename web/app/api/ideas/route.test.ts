import { describe, it, expect } from 'vitest';
import { POST } from './route';

describe('POST /api/ideas', () => {
  it('returns 200 for valid payload', async () => {
    const payload = { title: 'Idea', description: 'Great', userId: 'user123' };
    const req = new Request('http://localhost', {
      method: 'POST',
      body: JSON.stringify(payload),
      headers: { 'Content-Type': 'application/json' },
    });
    const res = await POST(req);
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body).toEqual({ success: true, data: payload });
  });

  it('returns 400 with details for invalid payload', async () => {
    const payload = { title: '', description: 123, userId: '' };
    const req = new Request('http://localhost', {
      method: 'POST',
      body: JSON.stringify(payload),
      headers: { 'Content-Type': 'application/json' },
    });
    const res = await POST(req);
    expect(res.status).toBe(400);
    const body = await res.json();
    expect(Array.isArray(body.errors)).toBe(true);
    expect(body.errors.length).toBeGreaterThan(0);
  });
});

