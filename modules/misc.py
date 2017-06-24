import discord
from discord.ext import commands

#import sys
import random
from time import time
from asyncio import sleep
from settings import MASTERS
from utils import remove_command
from functools import reduce

# Cleverbot support ;)
import cleverbot
cb = cleverbot.CleverBot(user='wZWeENyqMK96oI7V', key='Ueps0IU4HHVsvQUJ8F2L5NbTcYAiq5Xz', nick='discord')

random.seed(time())

class misc(object):
    def __init__(self, bot):
        self.bot = bot
        #self.nextnick = None
    @commands.command(pass_context=True)
    async def echo(self, ctx):
        if ctx.message.author.id in MASTERS: 
            await self.bot.say(remove_command(ctx.message.content))
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True, description='[NON-ADMIN] Ping Larry to check connectivity')
    async def ping(self, ctx):
        #if ctx.message.author.id in MASTERS:
        start = time()
        await self.bot.say('Pong!')
        end = time()
        await self.bot.say('Time taken: {} seconds'.format(round(end - start, 4)))
        #else:
        #    await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True, description='[NON-ADMIN] Say something to Larry! Anything!')
    async def ask(self, ctx): 
        question = remove_command(ctx.message.content)
        answer = cb.query(question)
        await self.bot.say(answer)
    @commands.command(pass_context=True)
    async def next(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('*Ding!* Next please!')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def dice(self, ctx):
        if ctx.message.author.id in MASTERS:
            sides = remove_command(ctx.message.content)
            try:
                side = str(random.randrange(1, int(sides) + 1))
            except ValueError:
                side = str(random.randrange(1, 7))
            await self.bot.say(side)
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command()
    async def whoisyourmaster(self):
        await self.bot.say('Kira is my Supreme Overlord and Master of the Seventeen Dimensions')
    @commands.command(pass_context=True)
    async def sleep(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.say('Nighty night.')
            await sleep(2)
            raise KeyboardInterrupt
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
#    @commands.command(pass_context=True)
#    async def changenick(self, ctx):
#        if ctx.message.author.id in MASTERS:
#            victim = remove_command(ctx.message.content)
#            try:
#                for member in ctx.message.server.members:
#                    if member.name == victim.strip():
#                        await self.bot.change_nickname(member, self.nextnick)
#                else:
#                    await self.bot.say('Could not find {}'.format(victim))
#            except discord.Forbidden:
#                await self.bot.say('Do not have proper permissions for that action')
#        else:
#            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
#    @commands.command(pass_context=True)
#    async def setnick(self, ctx):
#        if ctx.message.author.id in MASTERS:
#            self.nextnick = remove_command(ctx.message.content)
#        else:
#            await self.bot.say('You are not my master, {}'.format(ctx.message.author))

def setup(bot):
    bot.add_cog(misc(bot))
