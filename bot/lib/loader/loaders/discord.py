from lib.loader import FileLoader
from discord.ext.commands import Bot
from lib.debug import Debug

class DiscordCogLoader(FileLoader):
    """
        Loads discord cogs
    """
    def __init__(
            self, 
            debug: Debug, 
            auto_load: bool = True, 
            path: str = "cogs", 
            bot: Bot = None,
        ):
        
        if not bot:
            raise ValueError("Bot is required")
        
        super().__init__(auto_load=False, debug=debug, path=path)

        self.bot = bot

        if auto_load:
            self.load()

    def load(self, run_func_name: str="setup", *args, **kwargs):
        """
            Loads discord cogs to the specified bot
        """
        super().load(run_func_name=run_func_name, bot=self.bot, *args, **kwargs)