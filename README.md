# Clovis

**Make Poke sound like you.**

Clovis is an MCP (Model Context Protocol) integration designed for [Poke by interaction.co](https://poke.co) that enables truly personalized AI communication. By analyzing your email writing patterns, Clovis teaches Poke to mirror your unique communication style—your tone, your vocabulary, your formality level—making every interaction feel authentically you.

> **Note:** Clovis is a forward-looking integration feature **not yet available** in Poke. This MCP server demonstrates how future versions of Poke could leverage protocol-level personalization to become more than just an AI assistant—it becomes your digital communication persona.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/InteractionCo/mcp-server-template)

## Why Clovis Matters

Current AI assistants use generic, one-size-fits-all communication styles. Clovis changes this by:

- **Analyzing your actual writing** from email communications to understand your personal style
- **Categorizing your contacts** (friends, colleagues, support) to apply contextually appropriate tones
- **Generating style profiles** that capture your sentence patterns, emoji usage, formality, and signature phrases
- **Enabling Poke to communicate as you would**—not as a generic AI, but as your authentic digital self

This is the future of AI interaction: not tools that make you adapt to them, but tools that adapt to you.

## How It Works

Clovis provides specialized MCP tools for deep communication analysis:

### 1. `greet`
Greet a user by name with a welcome message from the MCP server.

**Parameters:**
- `name` (str): The name of the user to greet

**Returns:** A personalized greeting message

### 2. `get_server_info`
Get comprehensive information about the MCP server including name, version, environment, and Python version.

**Returns:** Dictionary with:
- `server_name`: Name of the MCP server
- `version`: Current version (1.0.0)
- `environment`: Running environment (development/production)
- `python_version`: Python runtime version

### 3. `getEmail`
Fetch emails from user contacts for persona generation and analysis.

**Parameters:**
- `email` (str): Email address to fetch related contacts for

**Returns:** List of email addresses associated with the user

### 4. `analyzeWriting`
Analyze the writing style from user contact emails and create a pattern based on the communication style.

**Parameters:**
- `emails` (list): List of email addresses to analyze

**Returns:** Dictionary with:
- `tone`: Communication tone ("formal" or "casual")
- `average_sentence`: Average sentence length
- `freq_emojis`: Emoji usage frequency
- `repeated_terms`: Commonly used words and phrases
- `signatures`: Common email signatures
- `formality_index`: Formality score (0.0-1.0)

### 5. `setCluster`
Categorize contacts into groups based on contact type (friends, work, support).

**Parameters:**
- `email` (str): Email address to categorize

**Returns:** Dictionary with:
- `cluster`: Category ("friend", "corporate", "support", or "unknown")

## Local Development

### Prerequisites

- Python 3.13 or higher
- Conda (recommended) or Python venv
- Node.js (for testing with MCP Inspector)

### Setup

1. Clone the repository:
```bash
git clone <your-repo-url>
cd clovis
```

2. Create and activate a virtual environment:
```bash
# Using Conda (recommended)
conda create -n mcp-server python=3.13
conda activate mcp-server

# OR using Python venv
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Server

Start the MCP server locally:
```bash
python src/server.py
```

The server will start on `http://0.0.0.0:8000` by default. You can customize the port using the `PORT` environment variable:
```bash
PORT=9000 python src/server.py
```

### Testing with MCP Inspector

1. Start the server (see above)

2. In another terminal, run the MCP Inspector:
```bash
npx @modelcontextprotocol/inspector
```

3. Open http://localhost:3000 in your browser

4. Connect to `http://localhost:8000/mcp` using "Streamable HTTP" transport

   **Important:** Make sure to include `/mcp` at the end of the URL!

5. Test the available tools through the inspector interface

## Deployment

### Option 1: One-Click Deploy to Render
Click the "Deploy to Render" button at the top of this README.

### Option 2: Manual Render Deployment
1. Fork this repository to your GitHub account
2. Sign in to [Render](https://render.com) and connect your GitHub account
3. Create a new Web Service
4. Connect your forked repository
5. Render will automatically detect the `render.yaml` configuration and deploy

Your deployed server will be available at:
```
https://your-service-name.onrender.com/mcp
```

**Important:** Always append `/mcp` to your server URL when connecting clients!

### Environment Variables

The following environment variables can be configured:

- `PORT`: Server port (default: 8000)
- `ENVIRONMENT`: Running environment (default: "development")

In production (Render), these are automatically set via `render.yaml`.

## Integration with AI Clients

### Claude Code / Poke Setup

1. Navigate to your AI client's settings/connections page
2. Add a new MCP server connection with your server URL (include `/mcp`)
3. Test the connection by asking the AI to use specific tools, e.g.:
   - "Use the greet tool to say hello to Alice"
   - "Analyze the writing style for these emails"
   - "What cluster does this email belong to?"

**Troubleshooting:**
- If the AI doesn't recognize your connection after renaming, try clearing the conversation history
- Ensure your URL includes the `/mcp` endpoint
- Verify the server is running and accessible

## Customization

### Adding New Tools

You can extend the server by adding new tools. Decorate functions with `@mcp.tool()`:

```python
@mcp.tool(description="Brief description of what this tool does")
def your_tool_name(param1: str, param2: int) -> dict:
    """
    Detailed documentation of the tool.

    Args:
        param1: Description of first parameter
        param2: Description of second parameter

    Returns:
        Description of return value
    """
    # Your implementation here
    return {"result": "your result"}
```

### Modifying Existing Tools

The email analysis tools in src/server.py:51-62 can be customized to:
- Connect to real email APIs (Gmail, Outlook, etc.)
- Implement actual ML-based writing analysis
- Store and retrieve contact clusters from a database
- Add more sophisticated persona generation

## Project Structure

```
clovis/
├── src/
│   └── server.py          # Main MCP server with tool definitions
├── requirements.txt       # Python dependencies
├── render.yaml           # Render deployment configuration
└── README.md            # This file
```

## Dependencies

- `fastmcp>=2.12.0` - FastMCP framework for building MCP servers
- `uvicorn>=0.35.0` - ASGI server for running the application

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly with MCP Inspector
5. Submit a pull request

## License

MIT License - feel free to use this server as a template for your own MCP projects.

## Support

For issues or questions:
- Check the [FastMCP documentation](https://github.com/jlowin/fastmcp)
- Review the [Model Context Protocol specification](https://modelcontextprotocol.io)
- Open an issue in this repository
