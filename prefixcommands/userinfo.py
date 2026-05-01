"""
Prefix Command: User Info

This module provides a command to display detailed information about a user.
Users can type `!userinfo` to see their own information or `!userinfo @mention`
to see information about another user.

Usage:
 !userinfo
 !userinfo @user

Dependencies:
 discord.py - For command framework and Discord API interaction
"""

import discord
from discord.ext import commands
from datetime import datetime


class UserInfo(commands.Cog):
    """A cog containing user information commands.

    This cog provides commands to display detailed information about Discord users,
    including their username, ID, join dates, and avatar URL.

    Args:
        bot: The bot instance that this cog is attached to. Required for
             accessing bot properties and sending responses.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the UserInfo cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @commands.command(name="userinfo", help="Display user information")
    async def userinfo(self, ctx: commands.Context, member: discord.Member = None) -> None:
        """Display detailed information about a user.

        This command shows comprehensive information about a Discord user,
        including their username, discriminator, user ID, server join date,
        account creation date, and avatar URL.

        Args:
            ctx: The command context containing message, channel, and author
                 information. Automatically provided by discord.py.
            member: Optional member mention. If not provided, shows info for
                    the command author. Must be a guild member.

        Returns:
            None. Sends an embed with user information to the channel.

        Notes:
            - If used in DMs (no guild context), shows an error message
            - If no member is mentioned, defaults to the command author
            - Dates are formatted in a user-friendly format (Month Day, Year)
            - All timestamps are shown in UTC

        Examples:
            >>> !userinfo
            (Shows your own information)
            >>> !userinfo @username
            (Shows information about @username)
        """
        # Check if command is used in DMs
        if ctx.guild is None:
            await ctx.send("❌ This command can only be used in a server!")
            return

        # If no member specified, use the command author
        if member is None:
            member = ctx.author

        # Format dates in a user-friendly way
        def format_date(date: datetime) -> str:
            """Format datetime object into a readable string."""
            return date.strftime("%B %d, %Y")

        # Create an embed to display user information
        embed = discord.Embed(
            title="User Information",
            description=f"Information about {member.mention}",
            color=member.color if member.color != discord.Color.default() else discord.Color.blue(),
            timestamp=datetime.utcnow()
        )

        # Add user avatar as thumbnail
        embed.set_thumbnail(url=member.display_avatar.url)

        # Add user information fields
        embed.add_field(
            name="👤 Username",
            value=f"{member.name}#{member.discriminator}",
            inline=True
        )
        
        embed.add_field(
            name="🆔 User ID",
            value=f"{member.id}",
            inline=True
        )
        
        embed.add_field(
            name="📅 Joined Server",
            value=format_date(member.joined_at),
            inline=True
        )
        
        embed.add_field(
            name="🗓️ Account Created",
            value=format_date(member.created_at),
            inline=True
        )

        # Add avatar URL as a clickable link
        embed.add_field(
            name="🖼️ Avatar URL",
            value=f"[Click here]({member.display_avatar.url})",
            inline=False
        )

        # Add footer with requester info
        embed.set_footer(
            text=f"Requested by {ctx.author.name}",
            icon_url=ctx.author.display_avatar.url
        )

        # Send the embed
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """Register the UserInfo cog with the bot.

    This function is called during bot initialization to load the
    UserInfo cog and make its commands available for use.

    Args:
        bot: The bot instance to register the cog with.

    Returns:
        None
    """
    await bot.add_cog(UserInfo(bot))