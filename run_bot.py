from config.config import Config
from bot.bot_client import get_bot

config = Config()

bot = get_bot()


@bot.event
async def on_ready():
 print("Bot online")


while True:
 bot.run(config.token)
