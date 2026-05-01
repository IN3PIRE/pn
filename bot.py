"""
Entry point for the PN Discord bot.

This module initializes and runs the bot, loading command and event cogs
from the `prefixcommands`, `slashcommands`, and `events` packages.

Configuration:
 The bot requires a DISCORD_TOKEN environment variable, which should be
 copied from .env.example to .env with a valid token.

Features:
 - Prefix commands (e.g., !ping, !uptime, !userinfo, !serverinfo)
 - Slash commands (e.g., /hello, /echo, /serverinfo, /userinfo, /avatar, /8ball, /choose, /ping)
 - Event handlers (e.g., on_message, on_member_join)
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Validate critical configuration
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError(
        "DISCORD_TOKEN not found!\n"
        "1. Copy .env.example to .env\n"
        "2. Replace YOUR_BOT_TOKEN_HERE with your actual bot token\n"
        "3. Get a token from https://discord.com/developers/applications"
    )

# Configure bot intents for required functionality
intents = discord.Intents.default()
intents.message_content = True  # Required for prefix commands and message events
intents.members = True  # Required for member-related commands like userinfo

# Initialize bot with prefix from environment (defaults to !)
bot = commands.Bot(command_prefix=os.getenv("PREFIX", "!"), intents=intents)


async def load_extensions() -> None:
    """Load all bot extensions (cogs) from predefined modules.

    This function attempts to load command and event cogs from their
    respective packages. It provides detailed logging for each module
    and gracefully handles import or loading failures.

    Args:
        None

    Raises:
        Exception: If a cog fails to load, the exception is caught and logged
        instead of crashing the bot. This allows partial bot functionality
        even if some cogs are broken.
    """
    for ext in [
        # Prefix commands
        "prefixcommands.ping",
        "prefixcommands.uptime",
        "prefixcommands.userinfo",
        "prefixcommands.serverinfo",
        # Slash commands - existing
        "slashcommands.hello",
        "slashcommands.echo",
        # New slash commands
        "slashcommands.serverinfo",
        "slashcommands.userinfo",
        "slashcommands.avatar",
        "slashcommands.8ball",
        "slashcommands.choose",
        "slashcommands.ping",
        # Event handlers
        "events.handlers",
    ]:
        try:
            await bot.load_extension(ext)
            print(f"Loaded extension: {ext}")
        except Exception as e:
            print(f"Failed to load {ext}: {e}")
            # Print full traceback for debugging during development
            import traceback
            traceback.print_exc()


@bot.event
async def setup_hook() -> None:
    """Called after the bot logs in but before it starts processing events.

    This hook routine does two critical tasks:
    1. Loads all command and event cogs/extensions
    2. Syncs slash commands with Discord (globally or per-guild if needed)

    Note:
    Slash command sync can take up to an hour for global commands,
    but is instant when done per-guild during development.

    Args:
        None

    Side Effects:
    - Registers all cogs and their commands/events
    - Syncs the command tree with Discord's API
    - Prints status messages to console
    """
    await load_extensions()
    # Sync slash commands once when the bot starts
    try:
        synced = await bot.tree.sync()
        print(f"Slash commands synced: {len(synced)} commands registered")
        print(f"Commands: {[cmd.name for cmd in synced]}")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    # Start the bot with the Discord token from environment
    bot.run(TOKEN)
