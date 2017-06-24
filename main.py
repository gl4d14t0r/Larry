import discord
from discord.ext import commands

import logging
import sys

from settings import TOKEN
from settings import MODULES_PATH

sys.path.insert(0, MODULES_PATH)

# Logging setup
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='larry.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('LARRY: At %(asctime)s called %(name)s: %(message)s'))
logger.addHandler(handler)

larry = commands.Bot(command_prefix=',', description='Heh ;)  https://www.youtube.com/watch?v=mm_niiQfeWc')

@larry.event
async def on_ready():
    logger.info('Logged in as {} with id {}'.format(larry.user.name, larry.user.id))
    print('Logged in as {} with id {}'.format(larry.user.name, larry.user.id))
    #await larry.change_presence(None)
    larry.load_extension('misc')
    larry.load_extension('network')
    larry.load_extension('animu')
    larry.load_extension('memes')
    larry.load_extension('playback')
    larry.load_extension('admin')
    larry.load_extension('info')

@larry.event
async def on_message(message):
    if message.channel.is_private and message.content.startswith('https://discord.gg/') and message.author != larry.user:
        try:
            invite = await larry.get_invite(message.content)
            if isinstance(invite.server, discord.Object):
                await larry.accept_invite(invite)
                await larry.send_message(message.channel, 'Joined the server.')
                logger.info('Joined server {0.server.name} via {1.author.name}'.format(invite, message))
                print('Joined server {0.server.name} via {1.author.name}'.format(invite, message))
            else:
                logger.info('Attempted to rejoin {0.server.name} via {1.author.name}'.format(invite, message))
                print('Joined server {0.server.name} via {1.author.name}'.format(invite, message))
                await larry.send_message(message.channel, 'Already in that server.')
        except Exception as e:
            logger.info('Failed to join a server invited by {0.author.name}'.format(message))
            print('Failed to join a server invited by {0.author.name}'.format(message))
            print(e)
            await larry.send_message(message.channel, 'Could not join server.')
        finally:
            return
    await larry.process_commands(message)

@larry.event
async def on_server_join(server):
    await larry.say('{} is a server for peasants, but I\'ll stay here anyways'.format(server.name))

@larry.event
async def on_member_ban(member):
    await larry.say('LOL. {} was cancerous enough to get himself banned.'.format(member.name))

@larry.event
async def on_member_unban(server, user):
    await larry.say('{} was given mercy on this very day'.format(user.name))    

def main():
    larry.loop.set_debug(True)
    larry.run(TOKEN)

if __name__ == '__main__':
    main()
