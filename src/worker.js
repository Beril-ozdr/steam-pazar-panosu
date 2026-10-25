export default {
  async fetch(request, env) {
    if (request.method !== "GET" && request.method !== "HEAD") {
      return new Response("Method Not Allowed", {
        status: 405,
        headers: { Allow: "GET, HEAD" },
      });
    }

    const key = request.headers.get("CF-Connecting-IP") || "anon";
    const { success } = await env.RATE_LIMITER.limit({ key });
    if (!success) {
      return new Response("Çok fazla istek. Lütfen biraz bekleyin.", {
        status: 429,
        headers: {
          "Retry-After": "60",
          "Content-Type": "text/plain; charset=utf-8",
        },
      });
    }

    const res = await env.ASSETS.fetch(request);
    const out = new Response(res.body, res);
    if (res.status === 200) {
      out.headers.set("Cache-Control", "public, max-age=300");
    }
    return out;
  },
};
