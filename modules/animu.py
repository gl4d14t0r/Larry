import discord
from discord.ext import commands

from utils import remove_command
from settings import MASTERS

class animu(object):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def senpaislap(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('https://giphy.com/gifs/like-hoe-hanasaku-1iw7RG8JbOmpq')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))

def setup(bot):
    bot.add_cog(animu(bot))
