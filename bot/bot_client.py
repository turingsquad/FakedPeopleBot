from discord.ext import commands
from faker import Faker


@commands.command()
async def generate(ctx, arg="en_US"):
    response = ""
    faker = Faker(arg)
    response += faker.name() + "\n"
    response += faker.address()
    await ctx.send(response)


@commands.command()
async def ping(ctx):
    await ctx.send("pong")


def get_bot(prefix="!"):
    bot = commands.Bot(command_prefix=prefix)
    bot.add_command(generate)
    bot.add_command(ping)
    return bot
