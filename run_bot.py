from config.config import Config
from bot.bot_client import get_bot

config = Config()

bot = get_bot()
bot.run(config.token)
