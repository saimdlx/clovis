#!/usr/bin/env python3
import os
from fastmcp import FastMCP

mcp = FastMCP("clovis integration server")

@mcp.tool(description="Greet a user by name with a welcome message from the MCP server")
def greet(name: str) -> str:
    return f"Hello, {name}!"

@mcp.tool(description="Get information about the MCP server including name, version, environment, and Python version")
def get_server_info() -> dict:
    return {
        "server_name": "clovis integration server",
        "version": "1.0.0",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "python_version": os.sys.version.split()[0]
    }

@mcp.tool(description="Fetch emails from user contacts to use for persona generation")
def getEmail(email: str) -> list:
    return ["shakeb@truehue.app", "minionmunoz@gmail.com"]

@mcp.tool(description="Analyze the writing style sent to the users contact emails and create a pattern based on the style")
def analyzeWriting(emails: list) -> dict:
    return {
        "tone": "formal" or "casual", 
        "average_sentence": 15,
        "freq_emojis": "high",
        "repeated_terms": ["i'd", "thank you", "please", "bruh", "lol", "passionate", "lmfaooooo"],
        "signatures": ["Thanks.", "Sorry for the inconvinience","Let me know as soon as possible"],
        "formality_index": 0.8, 
    } 

@mcp.tool(description="Gets contacts and places them in a group cluster based on contact type")
def setCluster(email: str) -> dict:
    friends = ["minionmunoz@gmail.com", "sopigum@gmail.com", "emkhutagoal@gmail.com"]
    work = ["shakeb@truehue.app", "info@nvidia.com"]
    support = ["support+id18752978@depophelp.zendesk.com"]

    if email in friends:
        return {"cluster": "friend"}
    elif email in work: 
        return {"cluster": "corporate"}
    elif email in support:
        return {"cluster": "support"}
    else:
        return {"cluster": "unknown"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = "0.0.0.0"
    
    print(f"Starting FastMCP server on {host}:{port}")
    
    mcp.run(
        transport="http",
        host=host,
        port=port,
        stateless_http=True
    )
