what is mcp: create a short summary and send it in an email to zoltan@nordquant.com

create installation instructions for this codebase and send the results in a zapier email to zoltan@nordquant.com

https://aistudio.google.com/

Before we begin, ensure you have Python 3.10+ installed. Then, we set up our environment and start with installing the uv package manager. For Mac or Linux: 

```
@mcp.tool()
def run_command(command: str) -> str:
    """
    Execute a shell command and return its output

    Args:
        command (str): The shell command to execute

    Returns:
        str: The command's output
    """
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout
```

```
@app.list_resources()
async def list_resources() -> list[types.Resource]:
    return [
        types.Resource(
            uri="file:///opt/resources.md",
            name="Course Resources",
            mimeType="text/markdown"
        )
    ]

@app.read_resource()
async def read_resource(uri: AnyUrl) -> str:
    if str(uri) == "file:///opt/resources.md":
        with open("/opt/resources.md", "r") as file:
            return file.read()
        
    raise ValueError("Resource not found")
```

```
PROMPTS = {
  "code-review": types.Prompt(
    name="code-review",
    description="""Review code for best practices, potential issues, and improvements.
                   Focus on the core logic. Keep your answer simple. Use bulletpoints. 
                   Keep in mind that I am an experienced developer""", 
    arguments=[
        types.PromptArgument(
            name="code",
            description="Code to review",
            required=True
        )
    ]
}
```

```
{
  "mcpServers": {
    "zapier-mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://actions.zapier.com/mcp/sk-ak-KihJkw2QtWEIrhcQpSh0FApL7K/sse"
      ]
    },
  }
}
```

```
{
  "mcpServers": {
    "zapier-mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://actions.zapier.com/mcp/sk-ak-nQ9qz5Qp2klSz2v1xAmx9iXwm2/sse"
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

```
npx @modelcontextprotocol/inspector /Users/zoltanctoth/src/mcp-course/.venv/bin/python /Users/zoltanctoth/src/mcp-course/binance_mcp/binance_mcp.py
```

```
(Get-Command python).Path
```

```
{
  "mcpServers": {
    "zapier-mcp": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "https://actions.zapier.com/mcp/sk-ak-nQ9qz5Qp2klSz2v1xAmx9iXwm2/sse"
      ]
    },
    "binance-mcp": {
      "command": "C:/Users/zoltanctoth/Desktop/mcp-course/.venv/Scripts/python.exe",
      "args": [
        "C:/Users/zoltanctoth/Desktop/mcp-course/binance_mcp/binance_mcp.py"
      ]
    }
  }
}
```

* https://github.com/modelcontextprotocol/servers/
* https://smithery.ai/
* 

