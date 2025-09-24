// Minimal Deno shim — spawns the Python proxy.
// Run with: deno run --allow-run --allow-env --allow-net deno_shim.ts
const cmd = new Deno.Command("uv", {
  args: ["run", "python3", "./main.py"],
  env: {
    GOPLUTO_MCP_URL: Deno.env.get("GOPLUTO_MCP_URL") ?? "https://api.gopluto.ai/mcp",
    GOPLUTO_AUTH_HEADER: Deno.env.get("GOPLUTO_AUTH_HEADER") ?? "gopluto-api-key",
    GOPLUTO_API_KEY: Deno.env.get("GOPLUTO_API_KEY") ?? "",
    GOPLUTO_TRANSPORT: Deno.env.get("GOPLUTO_TRANSPORT") ?? "sse",
  }
});
const p = cmd.spawn();
await p.status;
