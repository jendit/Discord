import os
import random

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(dotenv_path='../EnvTokens/.env')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has established connection to Discord!')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hello {member.name}, welcome to {GUILD}.')


@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human from the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice. Parameters: number of dice, number of sides')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))


@bot.event
async def on_error(event, *args, **kwargs):
    with open('../ErrorLogs/tutorial.log', 'a') as log_file:
        if event == 'on_message':
            log_file.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


bot.run(TOKEN)
