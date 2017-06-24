import discord
from discord.ext import commands

from utils import remove_command
from settings import MASTERS

import wikiapi
wiki = wikiapi.WikiApi()

import urbandict

class info(object):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def wiki(self, ctx):
        searchtext = remove_command(ctx.message.content)
        results = wiki.find(searchtext)
        article = wiki.get_article(results[0])
        await self.bot.say('Wikipedia results:\n\n\n*{}*\n\n{}\n\n{}'.format(article.heading, article.summary, article.image))
    @commands.command(pass_context=True)
    async def urbandict(self, ctx):
        searchtext = remove_command(ctx.message.content)
        results = urbandict.define(searchtext)
        await self.bot.say('{}\nExample: {}'.format(results[0]['def'], results[0]['example']))

def setup(bot):
    bot.add_cog(info(bot))
