"""
Slash Command: Echo

This module provides a simple echo slash command for the PN bot.
Users can invoke /echo with a message parameter to have the bot repeat it back.

Usage:
 /echo <message>

Features:
 - Accepts a required string parameter
 - Repeats the user's message back to them
 - Demonstrates slash command parameter handling
 - Works in both guilds and DMs

Dependencies:
 discord.py - Provides the commands framework and Discord API integration
"""

import discord
from discord.ext import commands


class Echo(commands.Cog):
    """A cog containing echo slash commands.

    This cog demonstrates the implementation of application commands with
    parameters. It provides a simple echo command that repeats user input,
    making it ideal for beginners learning slash command implementation.

    Slash commands provide a native Discord UI experience with autocomplete,
    permissions, and command discovery built-in.

    Args:
        bot: The bot instance that this cog is attached to. Used for
            registering commands and accessing bot functionality.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Echo cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @discord.app_commands.command(name="echo", description="Echo your message")
    @discord.app_commands.describe(message="The message to echo")
    async def echo(self, interaction: discord.Interaction, message: str) -> None:
        """Echo back the user's message.

        This slash command accepts a string parameter and responds with the
        same message. It demonstrates parameter handling, interaction
        responses, and serves as a foundation for more complex commands.

        Args:
            interaction: The Discord interaction object representing the
                slash command invocation. Contains information about the user,
                channel, guild, and the command itself. Automatically provided
                by discord.py when the command is invoked.
            message: The string parameter to echo back to the user. This is
                a required parameter that the user provides when invoking
                the command.

        Returns:
            None. Responds to the interaction with the echoed message.

        Notes:
            - Slash commands must be synced with Discord before they appear
                in the command list. This is handled in bot.py's setup_hook.
            - The response must be sent within 3 seconds, or the interaction
                will expire. For longer operations, use interaction.response.defer().
            - Using interaction.response.send_message() sends an immediate
                response visible only to the user who invoked the command if
                ephemeral=True is set.

        Example:
            >>> /echo Hello, world!
            Bot responds: "Hello, world!"
        """
        # Send immediate response to the interaction
        # No defer needed as this is a simple, fast operation
        await interaction.response.send_message(message)


async def setup(bot: commands.Bot) -> None:
    """Register the Echo cog with the bot.

    This function is called during bot initialization to load the
    Echo cog and register its slash command with the bot's command tree.

    Args:
        bot: The bot instance to register the cog with.

    Returns:
        None

    Note:
        This registers the command directly with the tree, making it
        available as a top-level slash command across all guilds (after sync).
    """
    bot.tree.add_command(Echo(bot).echo)
