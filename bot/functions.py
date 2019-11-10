from discord.ext import commands
from faker import Faker
import random


class Functions(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def generate(self, ctx, arg="en_US"):
        response = ""
        faker = Faker(arg)
        response += faker.name() + "\n"
        response += str(random.randint(18, 60)) + "\n"
        response += faker.job() + "\n"
        response += faker.address()
        print(response)
        await ctx.send(response)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong")


def setup(bot):
    bot.add_cog(Functions(bot))
