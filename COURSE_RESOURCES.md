# MCP Bootcamp Course Resources 

## General
* [Our Github Repository](https://github.com/zoltanctoth/mcp-course)
* [Slides](https://docs.google.com/presentation/d/1d3PYBUqYntgh6YHOPk4Va61B-b0ok1pRZWoJzA9Venc/edit?usp=sharing)
* [The Official MCP Homepage](https://modelcontextprotocol.io/)

## Environment Setup - Installation Guides
 * [Visual Studio Code](https://code.visualstudio.com/)
 * [Node JS]([https://code.visualstudio.com/](https://nodejs.org/en/download))
 * [Python]([https://code.visualstudio.com/](https://www.python.org/downloads/))
   * **Install Python version 3.10 / 3.11 / 3.12 - Version 3.13 might not be fully supported yet by some of the libraries we cover**
 * [Installing uv](https://docs.astral.sh/uv/getting-started/installation/)

### Claude and Cursor
 * [Claude Desktop Download](https://claude.ai/download)
 * [Cursor Download](https://www.cursor.com/)

## Finding and Integrating Third-Party MCPs
 * [Zapier](https://zapier.com)
 * [Zapier MCP](https://zapier.com/mcp)

### Integrating Zapier's MCP (code)
```
{
  "mcpServers": {
    "zapier-mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "<<<Paste the Zapier URL from zapier.com here, something like https://mcp.zapier.com/api/mcp/a/11353467/mcp>>>"
      ]
    }
  }
}
```

### Stopping Zaper's MCP server
You only need to use this tool when you have issues with Zapier opening Browser Windows:

1. Remove the Zapier MCP from Claude / Cursor (by editing the JSON config)
2. Execute the following command:
   - Mac/Linux:
     `ps -ef | grep -i zapier | grep -v grep | awk '{print $2}' | xargs kill`
   - Windows:
     `Get-Process | Where-Object { $_.Name -like '*zapier*' } | ForEach-Object { $_.Kill() }`


## Third-Party MCP hubs
* [Projects selected by Anthropic](https://github.com/modelcontextprotocol/servers)
* [Smithery](https://smithery.ai/)
* [Cursor Directory](https://cursor.directory/)

## Implementing Our Own MCP Server
* [Official Python MCP Docs](https://github.com/modelcontextprotocol/python-sdk)

### Getting The Python Interpreter's path
* On a Max/Linux: `which python`
* On Window: `(Get-Command python).Path | -replace '\\', '/'`

### Launching the MCP inspector
```
npx @modelcontextprotocol/inspector@0.16.2 <<PATH OF PYTHON>> <<PATH OF YOUR binance_mcp.py>>
```

### Adding Binance MCP to Claude / Cursor
This is just an example. Ensure that you replace the Python path and your `binance_mcp.py`'s path to the correct value:

```
{
  "mcpServers": {
    "zapier-mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "<<<Paste the Zapier URL from zapier.com here, something like https://mcp.zapier.com/api/mcp/a/11353467/mcp>>>"
      ]
    },
    "binance-mcp": {
      "command": "/Users/zoltanctoth/src/mcp-course/.venv/bin/python",
      "args": [
        "/Users/zoltanctoth/src/mcp-course/binance_mcp/binance_mcp.py"
      ]
    }
  }
}
```

## Publishing an MCP to the npm Registry

### Build / Install the project:
```
cd typescript_mcp
npm install
```

### Add your MCP to a host:
```
{
    "mcpServers": {
        "binance-ts-mcp": {
            "command": "npx",
            "args": [
                "<<FULL PATH TO YOUR LOCAL FOLDER>>/mcp-course/typescript_mcp"
            ]
        }
    }
}
```

### Publish the MCP to the npm Registry

* First, create an account on https://www.npmjs.com/

Now, execute these commands
```
npm login
npm publish
```

Access your MCP from the repository:
```
{
    "mcpServers": {
        "binance-ts-mcp": {
            "command": "npx",
            "args": [
                "<<add the `name` attribute's value from typescript_mcp/package.json here>>"
            ]
        }
    }
}

## Deploying MCPs to Render.com with SSE/Streamable HTTP
 1) Clone this repository: https://github.com/zoltanctoth/binance-mcp
 2) Step into the cloned repository's folder
 2) Create a virtualenv `virtualenv venv --python=python3.12`
 3) Activate the virtualenv
 4) Install requirements.txt: `pip install -r requirements.txt`
 5) Run the MCP locally: `python binance_mcp.py`
 6) Run the MCP Inspector: `npx @modelcontextprotocol/inspector`
 7) Follow the instructions and connect to `http://localhost:8897/sse` 

```

## MCP Clients and Debugging MCPs
* [LangChain and LangGraph](https://www.langchain.com/)
* [React Agents (optional reading)](https://react-lm.github.io/)
* [LangChain MCP Adapter GitHub](https://github.com/langchain-ai/langchain-mcp-adapters)
* [LangSmith](https://www.langchain.com/langsmith)

## Production-ready MCPs on Cloudflare and MCP security
* [Cloudflare's blog - #mcp tag](https://blog.cloudflare.com/tag/mcp/)
* [Cloudflare's MCP Deep Dive](https://blog.cloudflare.com/remote-model-context-protocol-servers-mcp/)
* [Cloudflare's Python MCP Repo](https://github.com/cloudflare/ai/tree/main/demos/python-workers-mcp)

### Creating a publicly available MCP on Cloudflare

You'll find there reference solution in the [ref_my-cloudflare-mcp-server-public](ref_my-cloudflare-mcp-server-public) folder.

Here is the URL we use for the hard-coded crypto price response:
```
https://mcp-course.s3.eu-central-1.amazonaws.com/public/hard-coded-price.json
```

```
# Create a template repo
npm create cloudflare@latest -- my-cloudflare-mcp-server-public --template=cloudflare/ai/demos/remote-mcp-authless

# Start it
cd my-cloudflare-mcp-server-public
np start

# Log in to CloudFlare
npx wrangler login

# Deploy App
npx wrangler deploy
```

### Adding GitHub OAuth Security
* [Cloudflare's OAuth template apps](https://github.com/cloudflare/ai/tree/main/demos)

The commands we execute:
```
npm create cloudflare@latest -- my-cloudflare-mcp-server-secure --template=cloudflare/ai/demos/remote-mcp-github-oauth
cd my-cloudflare-mcp-server-secure

npx wrangler secret put GITHUB_CLIENT_ID
npx wrangler secret put GITHUB_CLIENT_SECRET
npx wrangler secret put COOKIE_ENCRYPTION_KEY

npx wrangler kv namespace create "OAUTH_KV"

```

## Dockerizing MCPs

### Docker Intro

Here are the commands we executed:
```
docker build . -t hello
docker container prune
docker image ls
docker image rm <<image id>>
```

### simple-binance-mcp
Here are the commands we executed:
```
docker build . -t simple-binance-mcp
docker image ls
docker run simple-binance-mcp

# Setting up GitHub access -------------------------------
# Mac / Linux 
export GITHUB_TOKEN="<<<your token>>>"
# Windows PowerShell
[Environment]::SetEnvironmentVariable("GITHUB_TOKEN", "your_token_here", "User")

# Windows (cmd, not PowerShell)
setx GITHUB_TOKEN "your_token_here"
# --------------------------------------------------------

docker buildx build --platform linux/amd64 -t simple-binance-mcp -t ghcr.io/zoltanctoth/simple-binance-mcp . --load

docker push ghcr.io/zoltanctoth/simple-binance-mcp
```

## Deploying MCP to AWS
This is the command we use for building and AWS-compatible MCP Docker image
```
docker buildx build --platform linux/amd64 -t mcp/binance-mcp . --load
```

## Guillaume Raille - MCPAdapt / Huggingface Smolagents MCP & Real-World MCP Lessons Learned

About Guillaume:
   * [LinkedIn](https://www.linkedin.com/in/guillaumeraille/)
   * [SubstantAI](https://www.substant.ai/)
   * [MCPAdapt](https://github.com/grll/mcpadapt)
   
Links to Technologies / Articles / Concepts Guillaume mentions:
   * [Building Effectiv Agents (by Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
   * [zed Editor](https://zed.dev/)
   * [Cursor Rules](https://docs.cursor.com/context/rules)
   * [uvx](https://docs.astral.sh/uv/guides/tools/)
   * [Open MCP Proxy](https://github.com/grll/open-mcp-proxy)


## The MCP Roadmap
* [The official MCP Roadmap from Anthropic](https://modelcontextprotocol.io/development/roadmap)
