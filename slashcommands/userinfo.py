"""
Slash Command: User Info

This module provides a user information slash command for the PN bot.
Users can invoke /userinfo to see detailed information about a member.

Usage:
 /userinfo [member]

Features:
 - Shows user avatar and display name
 - Displays account creation date and join date
 - Shows roles and permissions
 - Displays activity status and rich presence
 - Shows voice channel status if applicable
 - Displays server-specific statistics (message count, etc.)

Dependencies:
 discord.py - Provides the commands framework and Discord API integration
"""

import discord
from discord.ext import commands
from datetime import datetime


class UserInfo(commands.Cog):
    """A cog containing user information slash commands.

    This cog provides commands to retrieve and display comprehensive
    information about Discord members in the server.

    Args:
        bot: The bot instance that this cog is attached to.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the UserInfo cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @discord.app_commands.command(name="userinfo", description="Display detailed user information")
    @discord.app_commands.describe(member="The member to get information about (defaults to you)")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None) -> None:
        """Display comprehensive user statistics.

        This slash command shows detailed information about a Discord member,
        including account details, server activity, roles, and current status.

        Args:
            interaction: The Discord interaction object representing the slash command invocation.
            member: The member to get information about. If not provided, shows info about the command invoker.

        Returns:
            None. Responds to the interaction with an embed containing user information.
        """
        # Default to the user who invoked the command if no member is specified
        if member is None:
            member = interaction.user
        
        # Check if we're in a guild context for full member info
        if not interaction.guild:
            await interaction.response.send_message("This command can only be used in a server!", ephemeral=True)
            return
        
        # Ensure we have a proper Member object for guild context
        if not isinstance(member, discord.Member):
            member = interaction.guild.get_member(member.id)
            if not member:
                await interaction.response.send_message("Could not find that member in this server.", ephemeral=True)
                return
        
        # Defer the response as this might take a moment
        await interaction.response.defer()
        
        # Create embed with user information
        embed = discord.Embed(
            title=f"👤 {member.display_name}",
            description=f"{member.mention}\nID: `{member.id}`",
            color=member.color if member.color != discord.Color.default() else discord.Color.blue()
        )
        
        # Add user avatar
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        elif member.display_avatar:
            embed.set_thumbnail(url=member.display_avatar.url)
        
        # Account creation date and server join date
        account_created = member.created_at.strftime("%B %d, %Y")
        account_age = (datetime.utcnow() - member.created_at).days
        joined_at = member.joined_at.strftime("%B %d, %Y") if member.joined_at else "Unknown"
        server_age = (datetime.utcnow() - member.joined_at).days if member.joined_at else 0
        
        embed.add_field(
            name="📅 Account Information",
            value=(f"**Created:** {account_created}\n"
f"**Account Age:** {account_age} days\nf**Joined Server:** {joined_at}\nf**Server Age:** {server_age} days"),
inlin