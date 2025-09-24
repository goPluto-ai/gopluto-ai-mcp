![Cover](public/cover.png)

# GoPluto MCP — Up‑to‑date Service Knowledge & Snippets in Any Prompt

[![Website](https://img.shields.io/badge/Website-gopluto.ai-blue)](https://gopluto.ai) [![MCP](https://img.shields.io/badge/MCP-HTTP%20Remote-green)](#)[![MCP Badge](https://lobehub.com/badge/mcp/gopluto-ai-gopluto-ai-mcp)](https://lobehub.com/mcp/gopluto-ai-gopluto-ai-mcp) [![MIT licensed](https://img.shields.io/badge/License-MIT-orange)](./LICENSE)

[![Install in Cursor (Remote)](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=gopluto&config=eyJ1cmwiOiJodHRwczovL2FwaS5nb3BsdXRvLmFpL21jcCIsImhlYWRlcnMiOnsiZ29wbHV0by1hcGkta2V5IjoiWU9VUl9BUElfS0VZIn19)
[<img alt="Install in Cursor (Local proxy)" src="https://img.shields.io/badge/Cursor-Install%20Local%20Proxy-0098FF?style=for-the-badge&logo=visualstudiocode&logoColor=white">](https://cursor.com/en/install-mcp?name=gopluto&config=eyJjb21tYW5kIjoidXYiLCJhcmdzIjpbInJ1biIsInB5dGhvbjMiLCIvQUJTT0xVVEUvUEFUSC9UTy9nb3BsdXRvLW1jcC9tYWluLnB5Il0sImVudiI6eyJHT1BMVVRPX01DUF9VUkwiOiJodHRwczovL2FwaS5nb3BsdXRvLmFpL21jcCIsIkdPUExVVE9fQVVUSF9IRUFERVIiOiJnb3BsdXRvLWFwaS1rZXkiLCJHT1BMVVRPX0FQSV9LRVkiOiJZT1VSX0FQSV9LRVkiLCJHT1BMVVRPX1RSQU5TUE9SVCI6InNzZSJ9fQ%3D%3D)

> GoPluto MCP lets AI coding assistants pull **fresh service/provider knowledge**, **routing rules**, and **ready‑to‑paste snippets** from GoPluto — right inside your prompt.

---

## ❌ Without GoPluto

- ❌ No guarantee of finding the right expert when you actually need them
- ❌ Made-up providers and broken flows waste time
- ❌ Constant context-switching between people slows you down

## ✅ With GoPluto

Add `use gopluto` in your prompt (or set a rule once) and the assistant fetches **live GoPluto context**:

- Fresh, verified provider knowledge pulled directly into your prompt
- instant provider matching hints & filters
- minimal payloads & code snippets for expert access in minutes

**Examples**
```txt
Draft a WhatsApp onboarding flow that asks for experts within minutes. use gopluto
```
```txt
Show me the minimal payload to create a Service Request and start matching experts in under 60 seconds. use gopluto
```

---

## 🛠️ Installation

### Requirements
- Any MCP‑capable client (Cursor, Claude Code, VS Code, Windsurf, Zed, etc.)
- **GoPluto API Key** (keep client‑side)
- Network access to `https://api.gopluto.ai/mcp`

**Auth header:** `gopluto-api-key: YOUR_API_KEY`

> If your client can’t attach headers to remote servers, use the included **local stdio proxy** (`main.py`) to add the header for you.

---

### Cursor

**One‑click (Remote HTTP)**

[![Install in Cursor (Remote)](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=gopluto&config=eyJ1cmwiOiJodHRwczovL2FwaS5nb3BsdXRvLmFpL21jcCIsImhlYWRlcnMiOnsiZ29wbHV0by1hcGkta2V5IjoiWU9VUl9BUElfS0VZIn19)

**Manual (Remote)**
```json
{
  "mcpServers": {
    "gopluto": {
      "url": "https://api.gopluto.ai/mcp",
      "headers": { "gopluto-api-key": "YOUR_API_KEY" }
    }
  }
}
```

**Local (stdio proxy)**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"],
      "env": {
        "GOPLUTO_MCP_URL": "https://api.gopluto.ai/mcp",
        "GOPLUTO_AUTH_HEADER": "gopluto-api-key",
        "GOPLUTO_API_KEY": "YOUR_API_KEY",
        "GOPLUTO_TRANSPORT": "sse"
      }
    }
  }
}
```

---

### Claude Code (CLI)

**Remote**
```sh
claude mcp add --transport http gopluto https://api.gopluto.ai/mcp \
  --header "gopluto-api-key: YOUR_API_KEY"
```

**Local**
```sh
claude mcp add gopluto -- uv run python3 /ABSOLUTE/PATH/TO/gopluto-mcp/main.py
```

---

### Windsurf

**Remote**
```json
{
  "mcpServers": {
    "gopluto": {
      "serverUrl": "https://api.gopluto.ai/mcp",
      "headers": { "gopluto-api-key": "YOUR_API_KEY" }
    }
  }
}
```

**Local**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  }
}
```

---

### VS Code (Copilot Chat MCP)

**Remote**
```json
"mcp": {
  "servers": {
    "gopluto": {
      "type": "http",
      "url": "https://api.gopluto.ai/mcp",
      "headers": { "gopluto-api-key": "YOUR_API_KEY" }
    }
  }
}
```

**Local**
```json
"mcp": {
  "servers": {
    "gopluto": {
      "type": "stdio",
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  }
}
```

---

### Cline

**Marketplace** → search **GoPluto** → **Install**

**Manual (Remote)**
```json
{
  "mcpServers": {
    "gopluto": {
      "url": "https://api.gopluto.ai/mcp",
      "type": "streamableHttp",
      "headers": { "gopluto-api-key": "YOUR_API_KEY" }
    }
  }
}
```

---

### Zed

```json
{
  "context_servers": {
    "GoPluto": {
      "command": {
        "path": "uv",
        "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
      }
    }
  }
}
```

---

### Augment Code

**UI** → Settings → Tools → **+ Add MCP** → Command:
```
uv run python3 /ABSOLUTE/PATH/TO/gopluto-mcp/main.py
```

**Manual**
```json
"augment.advanced": {
  "mcpServers": [
    {
      "name": "gopluto",
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  ]
}
```

---

### Roo Code

**Remote**
```json
{
  "mcpServers": {
    "gopluto": {
      "type": "streamable-http",
      "url": "https://api.gopluto.ai/mcp",
      "headers": { "gopluto-api-key": "YOUR_API_KEY" }
    }
  }
}
```

**Local**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  }
}
```

---

### Gemini CLI

**Remote**
```json
{
  "mcpServers": {
    "gopluto": {
      "httpUrl": "https://api.gopluto.ai/mcp",
      "headers": {
        "gopluto-api-key": "YOUR_API_KEY",
        "Accept": "application/json, text/event-stream"
      }
    }
  }
}
```

**Local**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  }
}
```

---

### Claude Desktop

**Remote**: Settings → Connectors → Add Custom Connector  
URL: `https://api.gopluto.ai/mcp`  
Header: `gopluto-api-key: YOUR_API_KEY`

**Local**: Developer settings → edit `claude_desktop_config.json`
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"],
      "env": {
        "GOPLUTO_MCP_URL": "https://api.gopluto.ai/mcp",
        "GOPLUTO_AUTH_HEADER": "gopluto-api-key",
        "GOPLUTO_API_KEY": "YOUR_API_KEY",
        "GOPLUTO_TRANSPORT": "sse"
      }
    }
  }
}
```

---

### Opencode

**Remote**
```json
"mcp": {
  "gopluto": {
    "type": "remote",
    "url": "https://api.gopluto.ai/mcp",
    "headers": { "gopluto-api-key": "YOUR_API_KEY" },
    "enabled": true
  }
}
```

**Local**
```json
"mcp": {
  "gopluto": {
    "type": "local",
    "command": ["uv","run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"],
    "enabled": true
  }
}
```

---

### JetBrains AI Assistant

Settings → Tools → AI Assistant → **Model Context Protocol (MCP)** → **+ Add** → **As JSON**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  }
}
```

---

### Kiro

```json
{
  "mcpServers": {
    "GoPluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"],
      "env": {},
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

---

### Trae

**Remote**
```json
{
  "mcpServers": {
    "gopluto": { "url": "https://api.gopluto.ai/mcp" }
  }
}
```

**Local**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "uv",
      "args": ["run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  }
}
```

---

### Bun / Deno (local)

**Bun**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "bunx",
      "args": ["uv","run","python3","/ABSOLUTE/PATH/TO/gopluto-mcp/main.py"]
    }
  }
}
```

**Deno**
```json
{
  "mcpServers": {
    "gopluto": {
      "command": "deno",
      "args": ["run","--allow-run","--allow-env","--allow-net","/ABSOLUTE/PATH/TO/gopluto-mcp/deno_shim.ts"]
    }
  }
}
```

---

### Docker (local HTTP)

`Dockerfile`
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt main.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENV GOPLUTO_MCP_URL=https://api.gopluto.ai/mcp \
    GOPLUTO_AUTH_HEADER=gopluto-api-key \
    GOPLUTO_TRANSPORT=sse
EXPOSE 12006
CMD ["python","main.py","--mode","http","--host","0.0.0.0","--port","12006"]
```

Run:
```bash
docker build -t gopluto-mcp .
docker run --rm -p 12006:12006 -e GOPLUTO_API_KEY=YOUR_API_KEY gopluto-mcp
```

Point your client to `http://localhost:12006`.

---

### Windows notes
If paths/quoting are tricky, use `cmd /c` or PowerShell; prefer absolute paths for `command` and `args`.

---

## 🔧 Available Tools (examples)

- `resolve-gopluto-id` – Resolve a package/service name to a GoPluto ID  
- `get-gopluto-docs` – Fetch docs/snippets for a GoPluto ID  
- `search-providers` – Query providers by skills/geo/budget  
- `create-service-request` – Minimal payload helper

*(Your upstream server’s tool list may evolve; use your client’s tool inspector to list them.)*

---

## 🛟 Tips

**Add a Rule to auto‑use GoPluto**
```txt
Always use gopluto when I ask for service matching, onboarding flows, or API payloads.
Automatically call GoPluto MCP tools to resolve IDs and fetch snippets.
```

**HTTPS Proxy**: standard `HTTPS_PROXY` / `https_proxy` env variables apply.

---

## 💻 Development (local proxy)

```bash
uv pip install -r requirements.txt
export GOPLUTO_API_KEY="YOUR_REAL_KEY"
uv run python3 main.py               # stdio (default)
# or:
uv run python3 main.py --mode http --port 12006
```

**Smoke test remote server**
```bash
curl -X POST "https://api.gopluto.ai/mcp" \
  -H "Content-Type: application/json" \
  -H "gopluto-api-key: $GOPLUTO_API_KEY" \
  -d '{"jsonrpc":"2.0","id":"1","method":"initialize","params":{"protocolVersion":"2025-06-18"}}'
```

---

## 🚨 Troubleshooting

- **401/403** → wrong/missing `gopluto-api-key`
- **Client can’t add headers** → use local stdio proxy
- **TLS issues** → set `SSL_CERT_FILE` for Python
- **Module not found (Node)** → prefer Python proxy (no Node needed)

---

## 📄 License

MIT
