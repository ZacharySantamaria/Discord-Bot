"""The main of the bot"""

from os import getenv
from discord.ext import commands
from dotenv import load_dotenv
import discord


bot = commands.Bot(command_prefix=['~', 'bot '])
startup_extensions = ['functionality']


@bot.event
async def on_ready():
    """Once the bot is connected this startup function for the bot"""
    await bot.change_presence(
      activity=discord.Activity(type=discord.ActivityType.playing, name="with your mother"))

    for extension in startup_extensions:
        bot.load_extension(extension)

    print('Bot is connected')


load_dotenv()
TOKEN = getenv('TOKEN')

bot.run(TOKEN)
