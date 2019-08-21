# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv(dotenv_path='../EnvTokens/.env')
token = os.getenv('DISCORD_TOKEN')


class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')


client = CustomClient()
client.run(token)
