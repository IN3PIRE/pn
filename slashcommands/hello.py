"""
Slash Command: Hello

This module provides a simple greeting slash command for the PN bot.
Users can invoke /hello to receive a friendly welcome message from the bot.

Usage:
    /hello

Features:
    - Simple, intuitive greeting
    - Immediate response
    - Demonstrates slash command implementation pattern

Dependencies:
    discord.py - Provides the commands framework and Discord API integration
"""

import discord
from discord.ext import commands


class Hello(commands.Cog):
    """A cog containing greeting slash commands.

    This cog demonstrates the implementation of application commands (slash
    commands) in discord.py. It provides a simple greeting command that can
    be invoked by any user in a server where the bot is present.

    Slash commands provide a native Discord UI experience with autocomplete,
    permissions, and command discovery built-in.

    Args:
        bot: The bot instance that this cog is attached to. Used for
            registering commands and accessing bot functionality.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Hello cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @discord.app_commands.command(name="hello", description="Say hello")
    async def hello(self, interaction: discord.Interaction) -> None:
        """Send a friendly greeting message.

        This slash command responds with a simple "Hello, world! 👋" message
        when invoked by a user. It serves as a basic example of slash command
        implementation and provides immediate visual feedback.

        Args:
            interaction: The Discord interaction object representing the
                slash command invocation. Contains information about the user,
                channel, guild, and the command itself. Automatically provided
                by discord.py when the command is invoked.

        Returns:
            None. Responds to the interaction with a greeting message.

        Notes:
            - Slash commands must be synced with Discord before they appear
              in the command list. This is handled in bot.py's setup_hook.
            - The response must be sent within 3 seconds, or the interaction
              will expire. For longer operations, use interaction.response.defer().
            - Using interaction.response.send_message() sends an immediate
              response visible only to the user who invoked the command if
              ephemeral=True is set.

        Example:
            >>> /hello
            Bot responds: "Hello, world! 👋"
        """
        # Send immediate response to the interaction
        # No defer needed as this is a simple, fast operation
        await interaction.response.send_message("Hello, world! 👋")


async def setup(bot: commands.Bot) -> None:
    """Register the Hello cog with the bot.

    This function is called during bot initialization to load the
    Hello cog and register its slash command with the bot's command tree.

    Args:
        bot: The bot instance to register the cog with.

    Returns:
        None

    Note:
        This registers the command directly with the tree, making it
        available as a top-level slash command across all guilds (after sync).
    """
    bot.tree.add_command(Hello(bot).hello)
