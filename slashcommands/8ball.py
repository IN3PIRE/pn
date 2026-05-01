"""
Slash Command: 8-Ball

This module provides a magic 8-ball slash command for the PN bot.
Users can ask the 8-ball a question and receive a random prediction.

Usage:
 /8ball <question>

Features:
 - Responds with random predictions from a curated list
 - Supports classic magic 8-ball responses
 - Interactive and engaging for users
 - Question parameter for user input

Dependencies:
 discord.py - Provides the commands framework and Discord API integration
 random - Python standard library for random responses
"""

import discord
from discord.ext import commands
import random


class EightBall(commands.Cog):
    """A cog containing 8-ball prediction slash commands.

    This cog provides a fun magic 8-ball command that gives random
    predictions in response to user questions.

    Args:
        bot: The bot instance that this cog is attached to.
    """

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the 8Ball cog.

        Args:
            bot: The bot instance to attach this cog to.
        """
        self.bot = bot
        
        # Define 8-ball responses following the classic magic 8-ball format
        self.responses = [
            # Positive responses (10)
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            # Neutral responses (5)
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            # Negative responses (5)
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

    @discord.app_commands.command(name="8ball", description="Ask the magic 8-ball a question")
    @discord.app_commands.describe(question="Your question for the magic 8-ball")
    async def eightball(self, interaction: discord.Interaction, question: str) -> None:
        """Ask the magic 8-ball a question and get a prediction.

        This slash command takes a user's question and responds with a random
        prediction from the magic 8-ball's repertoire of responses.

        Args:
            interaction: The Discord interaction object representing the slash command invocation.
            question: The question to ask the magic 8-ball (required parameter).

        Returns:
            None. Responds to the interaction with an embed containing the prediction.
        """
        # Get a random response from our predefined list
        response = random.choice(self.responses)
        
        # Determine embed color based on response type
        if response in ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.",
                        "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes."]:
color = discord.Color.green()
itral in ["Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
itrate now."]:	color = discord.Color.gold()
color = discord.Color.red()
color = discord.Color.red()
color = discord.Color.red()
color = discord.Color.red()