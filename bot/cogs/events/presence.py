import discord
from discord.ext import commands
from lib.debug import Debug

class BasicEvents(commands.Cog):
    def __init__(self, bot: commands.Bot, debug: Debug):
        self.bot = bot
        self.debug = debug

    @commands.Cog.listener()
    async def on_ready(self):
        """
            Event triggered when the bot is ready.
            Updates the bot's status.
        """

        # Debugs
        self.debug.print(f'Logged on as {self.bot.user}')

        await self.bot.tree.sync()

        # Update the status
        await self.bot.change_presence(activity=discord.Game(name="Monitoring logs..."))

async def setup(bot: commands.Bot, debug: Debug):
    await bot.add_cog(BasicEvents(bot, debug))