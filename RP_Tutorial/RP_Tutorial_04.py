# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path='../EnvTokens/.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user.name} has established connection to Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, welcome to {GUILD}.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human from the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('../ErrorLogs/tutorial.log', 'a') as log_file:
        if event == 'on_message':
            log_file.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


client.run(TOKEN)
