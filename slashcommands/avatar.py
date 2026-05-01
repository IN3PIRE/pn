"""
Slash Command: Avatar

This module provides an avatar slash command for the PN bot.
Users can invoke /avatar to display a user's profile picture at full size.

Usage:
 /avatar [member]

Features:
 - Displays user's avatar in full resolution
 - Shows server-specific avatar if available
 - Defaults to command invoker if no member specified
 - Shows avatar in a clean embed format

Dependencies:
 discord.py - Provides the commands framework and Discord API integration
"""

import discord
from discord.ext import commands


class Avatar(commands.Cog):
    """A cog containing avatar slash commands.

    This cog provides commands to display user avatars at full resolution.

    Args:
        bot: The bot instance that this cog is attached to.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Avatar cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @discord.app_commands.command(name="avatar", description="Display a user's avatar")
    @discord.app_commands.describe(member="The member whose avatar to show (defaults to you)")
    async def avatar(self, interaction: discord.Interaction, member: discord.Member = None) -> None:
        """Display a user's avatar at full resolution.

        This slash command shows a user's profile picture in full size.
        If the user has a server-specific avatar, it will be displayed.
        Otherwise, their global Discord avatar is shown.

        Args:
            interaction: The Discord interaction object representing the slash command invocation.
            member: The member whose avatar to display. If not provided, shows the command invoker's avatar.

        Returns:
            None. Responds to the interaction with an embed containing the avatar.
        """
        # Default to the user who invoked the command if no member is specified
        if member is None:
            member = interaction.user
        
        # Handle non-guild context gracefully
        if not isinstance(member, discord.Member):
            if interaction.guild:
                # Try to get proper Member object in guild context
                proper_member = interaction.guild.get_member(member.id)
                if proper_member:
                    member = proper_member
        
        # Create embed for avatar display
        embed = discord.Embed(
            title=f"🖼️ {member.display_name}'s Avatar",
            description=f"[Download Avatar]({member.display_avatar.url})",
            color=discord.Color.purple()
        )
        
        # Set the avatar image
        embed.set_image(url=member.display_avatar.url)
        
        # Add footer with user ID
        embed.set_footer(
            text=f"User ID: {member.id}",
            icon_url=member.display_avatar.url if hasattr(member.display_avatar, 'url') else None
        )
        
        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """Register the Avatar cog with the bot.

    Args:
        bot: The bot instance to register the cog with.
    """
    await bot.add_cog(Avatar(bot))