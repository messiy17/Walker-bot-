import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'welcome ')
    print('Sent message to ' + member.name)
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'welcome to the channel, I am Walker bot')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == '!hi':
        await client.send_message(message.channel,'!hi')
    if message.content.startswith('!coinflip'):
        randomlist = ["heads","tails"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!roast'):
        randomlist = ["fuck you","you big bitch",too ugly"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!welcome'):
        randomlist = ["welcome friends, I am Walker bot, nice to meet you"]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NTMyNTUzOTYxOTI0ODUzNzcx.Dxpfjw.wu5s33d0UfxbWvetxbS3iRKLJDY')
