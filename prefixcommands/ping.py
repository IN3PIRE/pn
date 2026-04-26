import discord
from discord.ext import commands

class Ping(commands.Cog):
    """Cog for prefix commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping", help="Check bot latency")
    async def ping(self, ctx: commands.Context) -> None:
        """Respond with latency info."""
        latency_ms = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! Latency: {latency_ms}ms")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))
