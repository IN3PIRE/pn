# bot.py
"""Entry point for the PN Discord bot.
It loads command and event cogs from the `prefixcommands`, `slashcommands`, and `events` packages.
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN not set in environment")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Load cogs (extensions)
async def load_extensions():
    for ext in [
        "prefixcommands.ping",
        "slashcommands.hello",
        "events.handlers",
    ]:
        try:
            await bot.load_extension(ext)
            print(f"Loaded extension: {ext}")
        except Exception as e:
            print(f"Failed to load {ext}: {e}")

@bot.event
async def setup_hook():
    await load_extensions()
    # Sync slash commands once when the bot starts
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")

if __name__ == "__main__":
    bot.run(TOKEN)
