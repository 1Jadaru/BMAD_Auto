import { z } from 'zod';

const ideaSchema = z.object({
  title: z.string().min(1, 'Title is required'),
  description: z.string().min(1, 'Description is required'),
  userId: z.string().min(1, 'User ID is required'),
});

export type Idea = z.infer<typeof ideaSchema>;

export async function POST(req: Request): Promise<Response> {
  try {
    const json = await req.json();
    const result = ideaSchema.safeParse(json);
    if (!result.success) {
      return new Response(
        JSON.stringify({ errors: result.error.issues }),
        {
          status: 400,
          headers: { 'Content-Type': 'application/json' },
        },
      );
    }

    return new Response(
      JSON.stringify({ success: true, data: result.data }),
      {
        status: 200,
        headers: { 'Content-Type': 'application/json' },
      },
    );
  } catch {
    return new Response(
      JSON.stringify({ errors: [{ message: 'Invalid JSON' }] }),
      {
        status: 400,
        headers: { 'Content-Type': 'application/json' },
      },
    );
  }
}

