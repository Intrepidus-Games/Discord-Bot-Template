from lib.loader.loaders.discord import DiscordCogLoader
from lib.debug import Debug
import discord
from discord.ext import commands

class BotManager:
    def __init__(self, 
            debug: Debug, 
            path: str = "cogs",
            intents: discord.Intents = None
        ):
        self.bot = commands.Bot(command_prefix="!", intents=intents)

        self.discord_loader = DiscordCogLoader(
            debug=debug,
            auto_load=False,
            path=path,
            bot=self.bot
        )

    def load(self):
        """
            Loads the cogs into the bot.
        """
        self.discord_loader.load(
            custom_param="custom_value"  # Example of passing custom parameters
        )

    def run(self, token):
        """
            Runs the bot with the provided token.
        """
        self.bot.run(token)

    def stop(self):
        """
            Stops the bot.
        """
        self.bot.close()

    def restart(self):
        """
            Restarts the bot.
        """
        self.stop()
        self.run(self.bot.token)