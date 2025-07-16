from discord import app_commands
from discord.ext import commands
from discord import Interaction
from lib.debug import Debug

class BasicCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, debug: Debug):
        self.bot = bot
        self.debug = debug

    @app_commands.command(name='ping', description='Check the bot\'s latency')
    async def ping(self, interaction: Interaction):
        """
            Responds with the bot's latency.
        """
        latency = round(self.bot.latency * 1000)  # Convert to milliseconds
        await interaction.response.send_message(f'Pong! Latency: {latency}ms')
        self.debug.print(f'Ping command executed. Latency: {latency}ms')

async def setup(bot: commands.Bot, debug: Debug):
    await bot.add_cog(BasicCommands(bot, debug))