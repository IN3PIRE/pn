"""
Slash Command: Server Info

This module provides a server information slash command for the PN bot.
Users can invoke /serverinfo to see detailed statistics about the server.

Usage:
 /serverinfo

Features:
 - Shows server name, ID, and icon
 - Displays member count (total, online, bots)
 - Shows server creation date and age
 - Lists server owner information
 - Shows verification level and boost status
 - Displays channel counts (text, voice, categories)
 - Shows role count and emoji count

Dependencies:
 discord.py - Provides the commands framework and Discord API integration
"""

import discord
from discord.ext import commands
from datetime import datetime


class ServerInfo(commands.Cog):
    """A cog containing server information slash commands.

    This cog provides commands to retrieve and display comprehensive
    information about the Discord server where the command is invoked.

    Args:
        bot: The bot instance that this cog is attached to.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the ServerInfo cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @discord.app_commands.command(name="serverinfo", description="Display detailed server information")
    async def serverinfo(self, interaction: discord.Interaction) -> None:
        """Display comprehensive server statistics.

        This slash command shows detailed information about the current server,
        including member counts, creation date, owner info, and various statistics.

        Args:
            interaction: The Discord interaction object representing the
            slash command invocation.

        Returns:
            None. Responds to the interaction with an embed containing server information.

        Notes:
            This command can only be used in a guild (server) context.
            It will fail if used in direct messages.
        """
        # Check if we're in a guild context
        if not interaction.guild:
            await interaction.response.send_message("This command can only be used in a server!", ephemeral=True)
            return

        # Defer the response as this might take a moment
        await interaction.response.defer()
        
        guild = interaction.guild
        
        # Calculate member statistics
        total_members = guild.member_count or 0
        online_members = len([m for m in guild.members if m.status != discord.Status.offline])
        bot_count = len([m for m in guild.members if m.bot])
        human_count = total_members - bot_count
        
        # Calculate channel statistics
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)
        categories = len(guild.categories)
        total_channels = text_channels + voice_channels + categories
        
        # Create embed with server information
        embed = discord.Embed(
            title=f"📊 {guild.name}",
            description=f"Server ID: `{guild.id}`",
            color=discord.Color.blue()
        )
        
        # Add server icon if available
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)
        
        # Member information field
        embed.add_field(
            name="👥 Member Statistics",
            value=(f"**Total:** {total_members:,}\n"
                   f"**Online:** {online_members:,}\n"
                   f"**Humans:** {human_count:,}\n"
                   f"**Bots:** {bot_count:,}"),
            inline=True
        )
        
        # Server age field
        creation_date = guild.created_at.strftime("%B %d, %Y")
        days_old = (datetime.utcnow() - guild.created_at).days
        embed.add_field(
            name="📅 Server Age",
            value=(f"**Created:** {creation_date}\n"
                   f"**Age:** {days_old} days"),
            inline=True
        )
        
        # Owner information field
        embed.add_field(
            name="👑 Owner",
            value=f"{guild.owner.mention if guild.owner else 'Unknown'}\n`{guild.owner_id}`",
            inline=True
        )
        
        # Channel information field
        embed.add_field(
            name="💬 Channels",
            value=(f"**Text:** {text_channels}\n"
                   f"**Voice:** {voice_channels}\n"
                   f"**Categories:** {categories}\n"
                   f"**Total:** {total_channels}"),
            inline=True
        )
        
        # Server features field (boosts, verification, etc.)
        boost_level = guild.premium_tier.name.replace("TIER_", "Level ")
        boost_count = guild.premium_subscription_count or 0
        verification_level = guild.verification_level.name.replace("_", " ").title()
        
        embed.add_field(
            name="⚡ Server Features",
            value=(f"**Boost Level:** {boost_level}\n"
f"**Boosts:** {boost_count}\nf"**Verification:** {verification_level}\nf"**Roles:** {len(guild.roles)}\nf"**Emojis:** {len(guild.emojis)}"),
inlin