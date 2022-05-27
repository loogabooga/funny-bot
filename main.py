# import discord.py
import discord
from discord.ext import commands
import os
import json


with open('cnofig.json') as f:
    config = json.load(f)


intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def reload(ctx):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.reload_extension(f'cogs.{filename[:-3]}')
            print(f'Reloaded {filename}')

# coghgers
for filename in os.listdir('cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config['token'], bot=True, reconnect=True)