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

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:
        """Send welcome message when a new member joins the server."""
        guild = member.guild
        
        # Try to get a welcome channel: system first, then general/default
        welcome_channel = guild.system_channel
        if welcome_channel is None:
            # Fallback to #general or first available text channel
            welcome_channel = discord.utils.get(guild.text_channels, name="general")
            if welcome_channel is None and guild.text_channels:
                welcome_channel = guild.text_channels[0]

        if welcome_channel:
            try:
                embed = discord.Embed(
                    title="👋 Welcome to the Server!",
                    description=f"Welcome {member.mention} to {guild.name}!",
                    color=discord.Color.green()
                )
                embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
                embed.add_field(name="Getting Started", value="Type `!help` to see available commands.", inline=False)
                embed.set_footer(text=f"Member #{guild.member_count}")
                
                await welcome_channel.send(embed=embed)
            except discord.Forbidden:
                print(f"Failed to send welcome message: Missing permissions in {welcome_channel}")
            except Exception as e:
                print(f"Failed to send welcome message: {e}")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EventHandlers(bot))
