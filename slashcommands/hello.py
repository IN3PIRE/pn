import discord
from discord.ext import commands

class Hello(commands.Cog):
    """Cog for slash commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @discord.app_commands.command(name="hello", description="Say hello")
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello, world! 👋")

async def setup(bot: commands.Bot) -> None:
    bot.tree.add_command(Hello(bot).hello)
    # Alternatively, you could add a Cog with @app_commands.command inside, but this registers directly.
