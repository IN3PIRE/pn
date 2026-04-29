"""
Prefix Command: Ping

This module provides a simple latency check command for the PN bot.
Users can type `!ping` to see the bot's current response time in milliseconds.

Usage:
    !ping

Dependencies:
    discord.py - For command framework and Discord API interaction
"""

import discord
from discord.ext import commands


class Ping(commands.Cog):
    """A cog containing bot utility commands.

    This cog provides basic diagnostic commands that help users and developers
    verify the bot is responsive and measure its current latency to Discord.

    Args:
        bot: The bot instance that this cog is attached to. Required for
            accessing bot properties like latency and sending responses.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Ping cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @commands.command(name="ping", help="Check bot latency")
    async def ping(self, ctx: commands.Context) -> None:
        """Respond with the bot's current latency in milliseconds.

        This command measures the time it takes for the bot to receive a
        heartbeat acknowledgement from Discord. It provides a simple way
        to verify the bot is online and responsive.

        Args:
            ctx: The command context containing message, channel, and author
                information. Automatically provided by discord.py.

        Returns:
            None. Sends a message to the channel where the command was invoked.

        Notes:
            Latency is calculated as the time between sending a heartbeat
            and receiving an acknowledgement, multiplied by 1000 to convert
            to milliseconds. This can fluctuate based on network conditions
            and Discord API response times.

        Example:
            >>> !ping
            Pong! Latency: 45ms
        """
        # Calculate latency in milliseconds (bot.latency is in seconds)
        latency_ms = round(self.bot.latency * 1000)

        # Send response with formatted latency value
        await ctx.send(f"Pong! Latency: {latency_ms}ms")


async def setup(bot: commands.Bot) -> None:
    """Register the Ping cog with the bot.

    This function is called during bot initialization to load the
    Ping cog and make its commands available for use.

    Args:
        bot: The bot instance to register the cog with.

    Returns:
        None
    """
    await bot.add_cog(Ping(bot))
