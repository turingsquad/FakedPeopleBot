from discord.ext import commands

extension = "bot.functions"


def get_bot(prefix="!"):
    bot = commands.Bot(command_prefix=prefix)
    bot.load_extension(extension)
    return bot
