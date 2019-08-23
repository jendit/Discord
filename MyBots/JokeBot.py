# bot.py
import os
import pyjokes
import discord

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path='../EnvTokens/.env')
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix='*')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('try *help for help'))
    print(f'{bot.user.name} has established connection to Discord!')


@bot.event
async def on_member(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, welcome to {GUILD}.')


@bot.command(name='joke', help='Provides a joke from PyJokes')
async def joke(ctx):
    response = pyjokes.get_joke()
    await ctx.send(response)


@bot.command(name='chuck', help='Provides a Chuck Norris programming joke')
async def chuck(ctx):
    response = pyjokes.get_joke('en', 'chuck')
    await ctx.send(response)


bot.run(TOKEN)