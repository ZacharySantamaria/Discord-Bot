"""The entry point of the discord bot"""

from os import getenv
import discord
from dotenv import load_dotenv
from discord.ext import commands
import asyncio



load_dotenv()
TOKEN = getenv('MAIN_TOKEN')
# ZACK_ID = getenv('ZACK_ID')
# print(ZACK_ID)
ZACK_ID = 288899751850672138
OMARI_ID = 443940248993398786
SANITA_ID = 438175368483176448
XAVI_ID = 186427201103593472
DONAL_ID = 357336111158263810
RYAN_ID = 290226329666977792
MEL_ID = 498000225374306324
CAIMAN_ID = 612872499515883521

intents = discord.Intents.default()
# intents.members = True
client = discord.Client(intents=intents)

"""Setting to the bots on ready"""
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.online, activity=game)

"""This event is used for looking through a new message and will find the specified authors and 
 will do an action. The current version is only reacting to the messages. Could possibly add 
 a counter and track however many types a person types then bans them"""
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Reaction for Zack
    elif message.author.id == ZACK_ID:
        await message.add_reaction("👔")

    # Reaction for Omari
    elif message.author.id == OMARI_ID:
        await message.add_reaction("🧸")

    # Reaction for Sanita
    elif message.author.id == SANITA_ID:
        await message.add_reaction("🍓")

    # Reaction for Donal
    elif message.author.id == DONAL_ID:
        await message.add_reaction("🍣")

    # Reaction for Ryan
    elif message.author.id == RYAN_ID:
        await message.add_reaction("🔥")

    elif message.author.id == MEL_ID:
        await message.add_reaction("💅")

    elif message.author.id == CAIMAN_ID:
        await message.add_reaction("🦂")

    else:
        print(f'{message.author} has typed {message.content}')

client.run(TOKEN)