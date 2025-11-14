"""The entry point of the discord bot"""

from os import getenv
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("MAIN_TOKEN")

# Getting specific IDs from people in the server
LANDO_ID = int(getenv("LANDO_ID"))
ZACK_ID = int(getenv("ZACK_ID"))
OMARI_ID = int(getenv("OMARI_ID"))
XAVI_ID = int(getenv("XAVI_ID"))
DONAL_ID = int(getenv("DONAL_ID"))
RYAN_ID = int(getenv("RYAN_ID"))
CAIMAN_ID = int(getenv("CAIMAN_ID"))

# Getting channel IDs
CHANNEL = int(getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.members = True  # pylint: disable=assigning-non-slot
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """Setting to the bots on ready"""
    print(f"We have logged in as {client.user}")
    game = discord.Game("programming with dad")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_member_join(member):
    """A custom message for new members that join.
    The idea is to base it off of chappie from the movie."""
    await member.send(
        "What's up fuck mother. I am a creation from my dad Zack. \
    I will eliminate you if you are mean. Have fun in the server!"
    )


@client.event
async def on_member_remove(member):
    """A cusom message will be made when someone is kicked or removed.
    This message will be somewhat based on the movie with my own twist."""
    general_channel = client.get_channel(CHANNEL)
    await general_channel.send(
        f"Sorry dad but I wanted to tell you that {member.name} \
        just left the server."
    )


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

    # Reaction for Donal
    elif message.author.id == DONAL_ID:
        await message.add_reaction("🍣")

    # Reaction for Ryan
    elif message.author.id == RYAN_ID:
        await message.add_reaction("🔥")

    elif message.author.id == CAIMAN_ID:
        await message.add_reaction("🦂")

    elif message.author.id == LANDO_ID:
        await message.add_reaction("🤓")

    else:
        print(f"{message.author} has typed {message.content}")


client.run(TOKEN)
