import discord
from discord.ext import commands

import subprocess
from utils import remove_command
from settings import MASTERS

class network(object):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(pass_context=True)
    async def scan(self, ctx):
        if ctx.message.author.id in MASTERS:
            options = remove_command(ctx.message.content)
            comm = ['nmap']
            comm.extend(options.split(' '))
            result = subprocess.Popen(comm, stdout=subprocess.PIPE)
            output = (result.communicate()[0]).decode('utf-8') 
            await self.bot.say(output)
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def geolocate(self, ctx):
        if ctx.message.author.id in MASTERS:
            ipaddr = remove_command(ctx.message.content)
            result = subprocess.Popen(['curl', 'freegeoip.net/xml/{}'.format(ipaddr)], stdout=subprocess.PIPE)
            output = (result.communicate()[0]).decode('utf-8')
            await self.bot.say(output)
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))

def setup(bot):
    bot.add_cog(network(bot))
