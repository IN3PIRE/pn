# bot.py
"""Starter Discord bot using discord.py (v2.x) with prefix commands, slash commands, and basic event handlers.

Features:
- Prefix command (`!ping`)
- Slash command (`/hello`)
- Event handlers: on_ready, on_message
- Uses intents and type hints for clarity.
"""

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load token from .env (or environment variable)
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN not set in environment")

# Define intents (adjust as needed)
intents = discord.Intents.default()
intents.message_content = True  # Required for on_message and prefix commands

# Create bot with command prefix '!'
bot = commands.Bot(command_prefix="!", intents=intents)

# ---------------- Prefix Commands ----------------
@bot.command(name="ping", help="Check bot latency")
async def ping(ctx: commands.Context) -> None:
    """Respond with latency info."""
    latency_ms = round(bot.latency * 1000)
    await ctx.send(f"Pong! Latency: {latency_ms}ms")

# ---------------- Slash Commands ----------------
@bot.tree.command(name="hello", description="Say hello")
async def hello(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Hello, world! 👋")

# ---------------- Event Handlers ----------------
@bot.event
async def on_ready() -> None:
    print(f"Bot is ready as {bot.user} (ID: {bot.user.id})")
    # Sync slash commands with Discord (register them)
    try:
        await bot.tree.sync()
        print("Slash commands synced.")
    except Exception as e:
        print(f"Failed to sync slash commands: {e}")

@bot.event
async def on_message(message: discord.Message) -> None:
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return
    # Simple keyword response example
    if "hello bot" in message.content.lower():
        await message.channel.send(f"Hello {message.author.mention}! 👋")
    # Ensure other commands still work
    await bot.process_commands(message)

# Run the bot
if __name__ == "__main__":
    bot.run(TOKEN)
