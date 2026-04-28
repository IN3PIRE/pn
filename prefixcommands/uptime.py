import discord
from discord.ext import commands
from datetime import datetime, timezone


class Uptime(commands.Cog):
    """Cog for the !uptime prefix command."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        # Record the moment this cog is loaded as the bot start time
        self.start_time: datetime = datetime.now(timezone.utc)

    @commands.command(name="uptime", help="Show how long the bot has been running")
    async def uptime(self, ctx: commands.Context) -> None:
        """Respond with the bot uptime in days, hours, minutes and seconds."""
        now = datetime.now(timezone.utc)
        delta = now - self.start_time

        total_seconds = int(delta.total_seconds())
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Build a human-readable string, omitting zero-value leading units
        parts: list[str] = []
        if days:
            parts.append(f"{days} day{'s' if days != 1 else ''}")
        if hours:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if minutes:
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")
        if not parts:
            # Bot just started — show seconds
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

        uptime_str = ", ".join(parts)
        await ctx.send(f"Bot Uptime: {uptime_str}")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Uptime(bot))
