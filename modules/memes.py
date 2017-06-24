import discord
from discord.ext import commands

from settings import MASTERS

import youtube_dl

class memes(object):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def birthplace(self, ctx):
        if ctx.message.author.id in MASTERS:    
            await self.bot.say('https://www.youtube.com/watch?v=mm_niiQfeWc')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def lookthroughwebcam(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('http://s2.storage.akamai.coub.com/get/b16/p/coub/simple/cw_timeline_pic/6bd93715fb6/d4aeef4ed9e93ffa7dfb3/big_1470421995_image.jpg')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def monday(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('https://giphy.com/gifs/monday-happy-mondays-are-the-worst-IlJ0FkaYggwkE')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def backoff(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('https://media.giphy.com/media/ilqP00AHM7vbIpq8P6/giphy.gif')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def shocking(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('https://media.giphy.com/media/d2ZbxughLGSLyPS0/giphy.gif')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def findnerd(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('*Larry points specifically to Matthew Lei*')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def findhomosexuals(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('*Larry suspiciously looks at Nelson and Brian*')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def findfuckboy(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('*Larry without hesitation points to Andrew Sugito*')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def whenautiststrytohaveanopinion(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('http://st.elohell.net/public/chill/71097b964c1aee2a4ad35de98eb6c26c.jpg')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))


def setup(bot):
    bot.add_cog(memes(bot))
