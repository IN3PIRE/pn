"""
Slash Command: Choose

This module provides a random choice slash command for the PN bot.
Users can provide multiple options and let the bot randomly select one.

Usage:
 /choose <option1> <option2> [option3] [option4] [option5]

Features:
 - Randomly selects from 2-5 provided options
 - Clean embed display of the chosen option
 - Useful for decision-making, games, and polls
 - Validates that at least 2 options are provided

Dependencies:
 discord.py - Provides the commands framework and Discord API integration
 random - Python standard library for random selection
"""

import discord
from discord.ext import commands
import random


class Choose(commands.Cog):
    """A cog containing random choice slash commands.

    This cog provides a choose command that randomly selects from
    multiple user-provided options.

    Args:
        bot: The bot instance that this cog is attached to.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Choose cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot

    @discord.app_commands.command(name="choose", description="Randomly choose between multiple options")
    @discord.app_commands.describe(
        option1="First option",
        option2="Second option",
        option3="Third option (optional)",
        option4="Fourth option (optional)",
        option5="Fifth option (optional)"
    )
    async def choose(
        self, 
        interaction: discord.Interaction, 
        option1: str,
        option2: str,
        option3: str = None,
        option4: str = None,
        option5: str = None
    ) -> None:
        """Randomly choose one option from a list.

        This slash command takes 2-5 options and randomly selects one,
        making it perfect for decision-making or adding randomness to activities.

        Args:
            interaction: The Discord interaction object representing the slash command invocation.
            option1: The first option to choose from (required).
            option2: The second option to choose from (required).
            option3: The third option to choose from (optional).
            option4: The fourth option to choose from (optional).
            option5: The fifth option to choose from (optional).

        Returns:
            None. Responds to the interaction with an embed containing the chosen option.
        """
        # Collect all provided options into a list
        options = [option1, option2]
        if option3:
            options.append(option3)
        if option4:
            options.append(option4)
        if option5:
            options.append(option5)
        
        # Validate that we have at least 2 options (enforced by required params, but good practice)
        if len(options) < 2:
aawait interaction.response.send_message("Please provide at least 2 options!", ephemeral=True)
rreturn
        		   # Randomly select one option   ition = random.choice(options)   		   # Create embed with the result  # Create embed with the result  # Create embed with the result  # Create embed with the result	il = "🎲 Random Choice"	       description="",		   color=discord.Color.random()		   )		   		   embed.add_field(			   name=f"Chosen from {len(options)} options:",			   value=f"**{chosen}**",			   inline=False		   )		   		   # List all options for context  	   options_text = "\".join(options)  	   if len(options_text) > 1000:  # Truncate if too long  	      options_text = options_text[:997] + "..."  	      embed.add_field(  	         name="All Options:",  	         value=options_text,  	         inline=False  	      )  	       # Set footer with requester info   embed.set_footer(  	      text=f"Requested by {interaction.user}",  	      icon_url=interaction.user.display_avatar.url if interaction.user.display_avatar else None  	   )  	       # Send response   await interaction.response.send_message(embed=embed)