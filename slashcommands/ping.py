"""
Slash Command: Ping

This module provides a ping slash command for the PN bot.
Users can invoke /ping to see the bot's latency and response time.

Usage:
 /ping

Features:
 - Shows bot latency (websocket ping)
 - Displays API response time
 - Shows uptime information
 - Clean embed display with status indicators

Dependencies:
 discord.py - Provides the commands framework and Discord API integration
 datetime - Python standard library for time calculations
"""

import discord
from discord.ext import commands
import datetime
import time


class Ping(commands.Cog):
    """A cog containing ping slash commands.

    This cog provides commands to check bot latency and performance metrics.

    Args:
        bot: The bot instance that this cog is attached to.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Ping cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot
        self.start_time = time.time()

    @discord.app_commands.command(name="ping", description="Check the bot's latency and performance")
    async def ping(self, interaction: discord.Interaction) -> None:
        """Display bot latency and performance metrics.

        This slash command shows the bot's websocket latency, API response time,
        and uptime information in a clean embed format.

        Args:
            interaction: The Discord interaction object representing the slash command invocation.

        Returns:
            None. Responds to the interaction with an embed containing latency information.
        """
        # Record start time for measuring response time
        start_time = time.time()
        
        # Defer the response
        await interaction.response.defer()
        
        # Calculate response time
        response_time = round((time.time() - start_time) * 1000)
        
        # Get websocket latency
        ws_latency = round(self.bot.latency * 1000)
        
        # Calculate uptime
        uptime_seconds = int(time.time() - self.start_time)
        uptime_string = str(datetime.timedelta(seconds=uptime_seconds))
        
        # Determine status based on latency (green < 100ms, yellow < 250ms, red otherwise)
        if ws_latency < 100:
            status_color = discord.Color.green()
            status_emoji = "🟢"
        elif ws_latency < 250:
            status_color = discord.Color.gold()	status_emoji = "🟡"
color = discord.Color.red()		   status_emoji = "🔴"		   		   # Create embed with performance metrics	tile = f"🏓 Pong! {status_emoji}",	color = status_color		   )		   		   embed.add_field(			   name="💓 WebSocket Latency",			   value=f"{ws_latency} ms",			   inline=True		   )		   		   embed.add_field(			   name="📝 API Response Time",			   value=f"{response_time} ms",			   inline=True		   )		   		   embed.add_field(			   name="⏰ Uptime",			   value=uptime_string,			   inline=True		   )		   		   # Add system information field	text=f"🤖 Bot: {self.bot.user}\f📦 Memory Usage: To be implemented"	# You could add actual memory usage tracking here if needed	text=f"🤖 Bot: {self.bot.user}\f📦 Guilds: {len(self.bot.guilds)}\f👥 Total Users: {sum(guild.member_count for guild in self.bot.guilds) if self.bot.guilds else 0}"	embed.add_field(	name="ℹ️ System Info",	value=text,	inlin