import discord
from discord.ext import commands

from settings import MASTERS
from utils import remove_command

class admin(object):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def kick(self, ctx):
        if ctx.message.author.id in MASTERS:
            victim = remove_command(ctx.message.content)
            try:
                for member in ctx.message.server.members:
                    if member.name == victim.strip():
                        await self.bot.kick(member)
                else:
                   await self.bot.say('Could not find {}'.format(victim))
            except discord.Forbidden:
                await self.bot.say('Do not have proper permissions for that action')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def ban(self, ctx):
        if ctx.message.author.id in MASTERS:
            victim = remove_command(ctx.message.content)
            try:
                for member in ctx.message.server.members:
                    if member.name == victim.strip():
                        await self.bot.ban(member)
                else:
                    await self.bot.say('Could not find {}'.format(victim))
            except discord.Forbidden:
                await self.bot.say('Do not have proper permissions for that action')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))

def setup(bot):
    bot.add_cog(admin(bot))
