# Clovis

**Make Poke sound like you.**

Clovis is an MCP (Model Context Protocol) integration designed for [Poke by interaction.co](https://poke.co) that enables truly personalized AI communication. By analyzing your writing patterns in depth, Clovis gives Poke the means to mirror your unique communication style—your tone, your vocabulary, your formality level—making every interaction feel authentically you.

> **Note:** Clovis is a forward-looking integration feature **not yet available** in Poke. This MCP server integration demonstrates Poke could leverage protocol-level personalization to become more than just an AI assistant, and instead your digital communication persona.

## Why Clovis Matters

Current AI assistants use generic, one-size-fits-all communication styles. Clovis changes this by:

- **Analyzing your actual writing** from email communications to understand your personal style
- **Categorizing your contacts** (friends, colleagues, support) to apply contextually appropriate tones
- **Generating style profiles** that capture your sentence patterns, emoji usage, formality, and signature phrases
- **Enabling Poke to communicate as you would**—not as a generic AI, but as your authentic digital self

This is the future of AI interaction: not tools that make you adapt to them, but tools that adapt to you.

## How It Works

Clovis provides specialized MCP tools for deep communication analysis:

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

## License

MIT License - feel free to use this server as a template for your own MCP projects.
