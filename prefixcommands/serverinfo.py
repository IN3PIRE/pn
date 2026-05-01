"""
Prefix Command: Server Info

This module provides a server information command for the PN bot.
Users can type `!serverinfo` to see basic statistics about the current Discord server.

Usage:
 !serverinfo

Dependencies:
 discord.py - For command framework and Discord API interaction
"""

import discord
from discord.ext import commands
from datetime import datetime


class ServerInfo(commands.Cog):
    """A cog containing server information commands.

    This cog provides commands that display information about the Discord server
    where the command is invoked, such as server name, member count, creation date,
    and server owner.

    Args:
        bot: The bot instance that this cog is attached to. Required for
        accessing bot properties and sending responses.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the ServerInfo cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @commands.command(name="serverinfo", help="Display server information")
    async def serverinfo(self, ctx: commands.Context) -> None:
        """Display information about the current Discord server.

        This command shows basic server statistics including the server name,
        total member count, creation date, and server owner. If used in a DM,
        it displays an error message instead.

        Args:
            ctx: The command context containing message, channel, and author
            information. Automatically provided by discord.py.

        Returns:
            None. Sends a message to the channel where the command was invoked.

        Notes:
            This command requires the command to be used within a server/guild.
            When used in direct messages, it will respond with an error message
            explaining that server information is only available in servers.

        Example:
            >>> !serverinfo
            Server: My Awesome Server
            Members: 42
            Created: January 15, 2023
            Owner: @username
        """
        # Check if command is used in a DM
        if ctx.guild is None:
            await ctx.send("❌ This command can only be used in a server!")
            return

        # Extract server information
        server_name = ctx.guild.name
        member_count = ctx.guild.member_count
        creation_date = ctx.guild.created_at
        owner = ctx.guild.owner

        # Format the creation date to be more readable
        formatted_date = creation_date.strftime("%B %d, %Y")

        # Format owner mention (handle case where owner might be None)
        owner_display = f"@{owner.name}" if owner else "Unknown"

        # Create the response message
        response = (
            f"**Server:** {server_name}\n"
            f"**Members:** {member_count}\n"
            f"**Created:** {formatted_date}\n"
            f"**Owner:** {owner_display}"
        )

        # Send the server information
        await ctx.send(response)


async def setup(bot: commands.Bot) -> None:
    """Register the ServerInfo cog with the bot.

    This function is called during bot initialization to load the
    ServerInfo cog and make its commands available for use.

    Args:
        bot: The bot instance to register the cog with.

    Returns:
        None
    """
    await bot.add_cog(ServerInfo(bot))