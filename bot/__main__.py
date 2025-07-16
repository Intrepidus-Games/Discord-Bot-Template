from lib.debug import Debug
from manager import BotManager
import discord
import dotenv
import os

# Load environment variables
dotenv.load_dotenv()

debug = Debug(
    log_info=os.getenv('LOG_INFO', 'True').lower() == 'true',
    log_warnings=os.getenv('LOG_WARNINGS', 'True').lower() == 'true',
    log_errors=os.getenv('LOG_ERRORS', 'True').lower() == 'true'
)

manager = BotManager(
    debug=debug, 
    path="bot/cogs",
    intents=discord.Intents.all()  # Set your desired intents here
)

# Load Manager Tasks
manager.load()

if __name__ == "__main__":
    # Run the bot with the token from the environment variable
    manager.run(os.getenv('DISCORD_TOKEN'))