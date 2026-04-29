"""
Prefix Command: Uptime

This module provides a bot uptime monitoring command for the PN bot.
Users can type !uptime to see how long the bot has been running since
its last restart.

Usage:
    !uptime

Features:
    - Tracks bot start time when cog loads
    - Calculates uptime in days, hours, minutes, seconds
    - Human-readable formatting (omits zero-value units)
    - Useful for monitoring bot stability and performance

Implementation:
    The cog records its initialization time (datetime.utcnow()) and
    calculates the delta between current time and start time when the
    command is invoked.

Dependencies:
    datetime - For precise time tracking and calculations
    discord.py - For command framework and Discord API
"""

import discord
from discord.ext import commands
from datetime import datetime, timezone


class Uptime(commands.Cog):
    """A cog that tracks and reports bot uptime statistics.

    This cog monitors how long the bot has been continuously running and
    provides a command to display this information in a human-readable format.
    It's useful for monitoring bot stability, tracking restart frequency,
    and providing transparency to users.

    The cog records its initialization timestamp and calculates uptime
    dynamically when the command is invoked, ensuring accurate reporting.

    Args:
        bot: The bot instance that this cog is attached to.

    Attributes:
        start_time: The UTC datetime when this cog was loaded, representing
            the bot's start time for uptime calculations.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Uptime cog and record start time.

        Args:
            bot: The bot instance to attach this cog to.

        Note:
            start_time is recorded as UTC to ensure consistent calculations
            across different time zones and daylight saving changes.
        """
        self.bot = bot
        # Record the moment this cog is loaded as the bot start time
        self.start_time: datetime = datetime.now(timezone.utc)

    @commands.command(name="uptime", help="Show how long the bot has been running")
    async def uptime(self, ctx: commands.Context) -> None:
        """Display bot uptime in human-readable format (days, hours, minutes, seconds).

        Calculates the time elapsed since the bot started and formats it
        as a readable string. Omits time units that are zero (e.g., won't show
        "0 days"), except will show seconds if the bot just started.

        Args:
            ctx: The command context containing the message, channel, author,
                and guild information. Automatically provided by discord.py.

        Returns:
            None. Sends a message with the formatted uptime string.

        Notes:
            The uptime calculation breaks down total seconds as follows:
            - 86400 seconds per day
            - 3600 seconds per hour
            - 60 seconds per minute

            The string formatting omits leading zero-value units for brevity.

        Example:
            >>> !uptime
            Bot Uptime: 2 days, 4 hours, 23 minutes

            >>> !uptime (if bot just started)
            Bot Uptime: 15 seconds
        """
        # Get current time in UTC for accurate calculation
        now = datetime.now(timezone.utc)

        # Calculate timedelta between now and bot start time
        delta = now - self.start_time

        # Convert total seconds to integer for divmod operations
        total_seconds = int(delta.total_seconds())

        # Break down total seconds into days, hours, minutes, seconds
        # 86400 seconds in a day, 3600 seconds in an hour
        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        # Build a human-readable string, omitting zero-value leading units
        parts: list[str] = []

        # Only add non-zero time units to the output string
        if days:
            # Handle pluralization for days
            parts.append(f"{days} day{'s' if days != 1 else ''}")

        if hours:
            # Handle pluralization for hours
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")

        if minutes:
            # Handle pluralization for minutes
            parts.append(f"{minutes} minute{'s' if minutes != 1 else ''}")

        if not parts:
            # Bot just started — show seconds with pluralization
            parts.append(f"{seconds} second{'s' if seconds != 1 else ''}")

        # Join all parts with commas for readability
        uptime_str = ", ".join(parts)

        # Send formatted uptime message to the channel
        await ctx.send(f"Bot Uptime: {uptime_str}")


async def setup(bot: commands.Bot) -> None:
    """Register the Uptime cog with the bot.

    This function is called during bot initialization to load the
    Uptime cog and make the !uptime command available.

    Args:
        bot: The bot instance to register the cog with.

    Returns:
        None

    Note:
        Once loaded, the cog begins tracking uptime immediately by recording
        the current time as start_time.
    """
    await bot.add_cog(Uptime(bot))
