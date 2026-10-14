# Schematic Renderer Bot

Render and manage Minecraft schematics directly in Discord.

## Features

- Render Minecraft schematics from .lite, .litematic, and .schematic files
- Create and manage schematic panels
- Organize schematics in threads for better management

## Requirements

- Python 3.8 or higher
- discord.py
- python-dotenv
- Pillow
- numpy
- schematics
- litematica
- pyworld

## Installation

1. Clone the repository:

```bash

git clone https://github.com/EnderDevelopment/schematic-renderer-bot.git
cd schematic-renderer-bot

```

2. Install the required dependencies:

```bash

pip install -r requirements.txt

```

3. Create a `.env` file based on `.env.example` and add your Discord bot token.

## Usage

1. Invite the bot to your Discord server.

2. Use the `/render` command to render a schematic file.

3. Use the `/schematic_panel` command to create a schematic panel.

4. Use the `/schematic_thread_create` command to create a new schematic thread.

5. Use the `/schematic_add` command to add a schematic to a thread.

## Configuration

The bot uses a `.env` file for configuration. Ensure you have the following variables set:

```env

DISCORD_TOKEN=your_discord_bot_token_here

```

---

## Generated with EnderDevelopment

This plugin was generated in minutes with [EnderDevelopment](https://enderdevelopment.com) — the AI platform that turns your ideas into working Minecraft plugins, Discord bots and FiveM scripts.

**Want your own?** [Generate this project on EnderDevelopment](https://dash.enderdevelopment.com?utm_source=github&utm_medium=readme&utm_campaign=schematic-renderer-bot&utm_content=bottom) — describe it in one sentence and get the full source code.
