"""The entry point of the discord bot"""

from os import getenv
import discord
from dotenv import load_dotenv



load_dotenv()
TOKEN = getenv('MAIN_TOKEN')
ZACK_ID = int(getenv('ZACK_ID'))
OMARI_ID = int(getenv('OMARI_ID'))
SANITA_ID = int(getenv('SANITA_ID'))
XAVI_ID = int(getenv('XAVI_ID'))
DONAL_ID = int(getenv('DONAL_ID'))
RYAN_ID = int(getenv('RYAN_ID'))
MEL_ID = int(getenv('MEL_ID'))
CAIMAN_ID = int(getenv('CAIMAN_ID'))

intents = discord.Intents.default()
# intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """Setting to the bots on ready"""
    print(f'We have logged in as {client.user}')
    game = discord.Game("with your mom")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    """This event is used for looking through a new message and will find the specified authors and
     will do an action. The current version is only reacting to the messages. Could possibly add
     a counter and track however many types a person types then bans them"""
    if message.author == client.user:
        return

    # Reaction for Zack
    if message.author.id == ZACK_ID:
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
