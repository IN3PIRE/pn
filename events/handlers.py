import discord
from discord.ext import commands

class EventHandlers(commands.Cog):
    """Cog for various event listeners."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        print(f"Bot is ready as {self.bot.user} (ID: {self.bot.user.id})")
        # Sync slash commands (in case not done elsewhere)
        try:
            await self.bot.tree.sync()
            print("Slash commands synced.")
        except Exception as e:
            print(f"Failed to sync slash commands: {e}")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return
        if "hello bot" in message.content.lower():
            await message.channel.send(f"Hello {message.author.mention}! 👋")
        # Ensure other commands still work
        await self.bot.process_commands(message)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EventHandlers(bot))
