"""Creation of a class to add functionality to the bot. These will be general things like
text listners and small commands."""
from discord.ext import commands
from requests import post
# import asyncio

ZACK_ID = 288899751850672138
YAS_ID = 474609160487698463
OMARI_ID = 443940248993398786
SANITA_ID = 438175368483176448
XAVI_ID = 186427201103593472
DONAL_ID = 357336111158263810

class Functionality(commands.Cog):
    """A class that holds the functionality of the bot"""
    def __init__(self, bot):
        self.count = 0
        self.bot = bot
        self.yas_count = 0
        self.omari_talked = False

    # Commands definitions

    # Text listener behavior
    @commands.Cog.listener('on_message')
    async def message_reponse(self, msg):
        """Command that will listen in general chat and give wanted responses"""
        # Tracking if Yasmine talked for the first time message
        # if msg.author.id == YAS_ID and self.yas_count == 0:
        #     await msg.reply('Please stop typing in this chat')
        #     self.yas_count += 1

        # After the first talked from Yasmine it will now track and give them 5 left talks until ban
        # elif msg.author.id == YAS_ID and self.yas_count > 0 and self.yas_count < 6:
        #     await msg.reply(f"You have { 5 - self.yas_count } messages left.")
        #     await msg.add_reaction("👎")
        #     self.yas_count += 1
        # Checks if Omari talks and will reply with a nice message
        if msg.author.id == OMARI_ID and self.omari_talked is not True:
            await msg.reply("Welcome back King")
            await msg.add_reaction("👑")
            self.omari_talked = True

        # Will always react to Omari's and I messages
        elif msg.author.id in (OMARI_ID, ZACK_ID):
            await msg.add_reaction("👑")

        # Reaction for Sanita
        elif msg.author.id == SANITA_ID:
            await msg.add_reaction("🍓")

        # Reaction for Xavi
        elif msg.author.id == XAVI_ID:
            await msg.add_reaction("🦙")

        # Reaction for Donal
        elif msg.author.id == DONAL_ID:
            await msg.add_reaction("🍣")

    # @commands.command()
    # async def deleteMsg(self, ctx, *, msg):
    #   await

    # @commands.Cog.listener('on_message')
    # async def spam(self, msg):
    #   if msg.author.id == self.ZackId and 'no' in msg.content:
    #     user = await self.bot.fetch_user(self.yasmineID)
    #     for i in range(10):
    #       await user.send("Stop Typing")
    #       await asyncio.sleep(1)
    @commands.command(name="ye")
    async def _ye(self, ctx):
        """Function that will display Kan(YE) quotes in "general" text channel"""
        ret = post('https://api.kanye.rest')
        self.count += 1
        await ctx.send(f"\"{ret.json()['quote']}\" - Kan(Ye) West")


def setup(bot):
    """Setup for the bot"""
    bot.add_cog(Functionality(bot))
