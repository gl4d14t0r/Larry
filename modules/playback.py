import discord
from discord.ext import commands

from utils import remove_command
from settings import MASTERS
from settings import MULTIM_PATH
from main import logger
from time import sleep
from tempfile import NamedTemporaryFile
from os import remove

import youtube_dl

import cleverbot
cb = cleverbot.CleverBot(user='wZWeENyqMK96oI7V', key='Ueps0IU4HHVsvQUJ8F2L5NbTcYAiq5Xz', nick='discord')

from gtts import gTTS

if not discord.opus.is_loaded():
    logger.info('Opus not loaded')
    print('Opus not loaded')

class playback(object):
    def __init__(self, bot):
        self.bot = bot 
        self.voice = None
        self.player = None 
    @commands.command(pass_context=True)
    async def join(self, ctx):
        if ctx.message.author.id in MASTERS:
            channame = remove_command(ctx.message.content)
            for channel in ctx.message.server.channels:
                if channel.type == discord.ChannelType.voice and channel.name == channame.strip():
                    self.voice = await self.bot.join_voice_channel(channel)
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def leave(self, ctx):
        if ctx.message.author.id in MASTERS:
            if self.bot.is_voice_connected(ctx.message.server):
                await self.voice.disconnect()
            else:
                self.bot.say('Not even connected in the first place')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def play(self, ctx):
        if ctx.message.author.id in MASTERS:
            url = remove_command(ctx.message.content) 
            if not self.bot.is_voice_connected(ctx.message.server):
                await self.bot.say('Must be connected to voice channel')
                return
            self.player = await self.voice.create_ytdl_player(url, use_avconv=False)
            await self.bot.change_presence(game=discord.Game(name='Playing '+self.player.title))
            self.player.start()
            await self.bot.say('Playing {}'.format(self.player.title))
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def stop(self, ctx):
        if ctx.message.author.id in MASTERS:
            await self.bot.change_presence(status=None)
            self.player.stop()
            await self.bot.say('Stopping...')
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def ohhh(self, ctx):
        if ctx.message.author.id in MASTERS:
            if not self.bot.is_voice_connected(ctx.message.server):
                await self.bot.say('Must be connected to voice channel')
                return
            self.player = self.voice.create_ffmpeg_player(MULTIM_PATH + 'shfoo.mp3', use_avconv=False)
            self.player.start()
            while self.player.is_playing():
                sleep(1)
            self.player.stop()
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def gayyy(self, ctx):
        if ctx.message.author.id in MASTERS:
            if not self.bot.is_voice_connected(ctx.message.server):
                await self.bot.say('Must be connected to voice channel')
                return
            self.player = self.voice.create_ffmpeg_player(MULTIM_PATH + 'hagay.mp3', use_avconv=False)
            self.player.start()
            while self.player.is_playing():
                sleep(1)
            self.player.stop()
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def askvoice(self, ctx):
        #if ctx.message.author.id in MASTERS:
            if not self.bot.is_voice_connected(ctx.message.server):
                await self.bot.say('Must be connected to voice channel')
                return
            question = remove_command(ctx.message.content)
            answer = cb.query(question)
            tts = gTTS(text=answer, lang='en-au', slow=False)
            tts.save(MULTIM_PATH + 'temp.mp3')
            ttsholder = open(MULTIM_PATH + 'temp.mp3')
            
            self.player = self.voice.create_ffmpeg_player(ttsholder.name, use_avconv=False)

            self.player.start()
            while self.player.is_playing():
                sleep(1)
            self.player.stop()
            remove(MULTIM_PATH + 'temp.mp3')
            ttsholder.close()
        #else:
            #await self.bot.say('You are not my master, {}'.format(ctx.message.author))
    @commands.command(pass_context=True)
    async def echovoice(self, ctx):
        if ctx.message.author.id in MASTERS:
            if not self.bot.is_voice_connected(ctx.message.server):
                await self.bot.say('Must be connected to voice channel')
                return
            echotext = remove_command(ctx.message.content)
            tts = gTTS(text=echotext, lang='en-au', slow=False)
            tts.save(MULTIM_PATH + 'tempecho.mp3')
            ttsholder = open(MULTIM_PATH + 'tempecho.mp3')

            self.player = self.voice.create_ffmpeg_player(ttsholder.name, use_avconv=False)

            self.player.start()
            while self.player.is_playing():
                sleep(1)
            self.player.stop()
            remove(MULTIM_PATH + 'tempecho.mp3')
            ttsholder.close()
        else:
            await self.bot.say('You are not my master, {}'.format(ctx.message.author))

def setup(bot):
    bot.add_cog(playback(bot))
