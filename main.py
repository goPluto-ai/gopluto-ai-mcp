import os, argparse
from fastmcp import FastMCP

def build_proxy():
    url = os.getenv("GOPLUTO_MCP_URL", "https://api.gopluto.ai/mcp")
    api_key = os.getenv("GOPLUTO_API_KEY", "").strip()
    auth_header = os.getenv("GOPLUTO_AUTH_HEADER", "gopluto-api-key")
    transport = os.getenv("GOPLUTO_TRANSPORT", "sse").lower()
    if not api_key:
        raise SystemExit("GOPLUTO_API_KEY is required")
    headers = {auth_header: api_key}
    return FastMCP.as_proxy(
        url=url, transport=transport, headers=headers,
        server_name="gopluto-mcp-proxy", server_version="1.0.0",
    )

def main():
    p = argparse.ArgumentParser(description="GoPluto MCP local proxy (stdio ↔ HTTP/SSE)")
    p.add_argument("--mode", choices=["stdio","http"], default="stdio")
    p.add_argument("--host", default="127.0.0.1")
    p.add_argument("--port", type=int, default=12006)
    a = p.parse_args()
    proxy = build_proxy()
    if a.mode == "http":
        print(f"[gopluto] MCP proxy listening on http://{a.host}:{a.port}")
        proxy.run_http(host=a.host, port=a.port)
    else:
        print("[gopluto] MCP proxy listening on stdio…")
        proxy.run_stdio()

if __name__ == "__main__":
    main()
