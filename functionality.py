from discord.ext import commands
from requests import post
# import asyncio

class functionality(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

    self.ZackId = 288899751850672138
    self.yasmineID = 474609160487698463
    self.omariID = 443940248993398786
    self.sanitaID = 438175368483176448
    self.xaviID = 186427201103593472
    self.donalID = 357336111158263810
    self.yasCount = 0
    self.omariTalked = False

  
  # Commands definitions
  @commands.command()
  async def ye(self, ctx):
    ret = post('https://api.kanye.rest')
    await ctx.send(f"\"{ret.json()['quote']}\" - Kan(Ye) West")

  # Text listener behavior
  @commands.Cog.listener('on_message')
  async def hi_detector(self, msg):
    
    # Tracking if Yasmine talked for the first time message
    if msg.author.id == self.yasmineID and self.yasCount == 0:
      await msg.reply('Please stop typing in this chat')
      self.yasCount += 1

    # After the first talked from Yasmine it will now track and give them 5 left talks until ban
    elif msg.author.id == self.yasmineID and self.yasCount > 0 and self.yasCount < 6:
      await msg.reply(f"You have { 5 - self.yasCount } messages left.")
      await msg.add_reaction("👎")
      self.yasCount += 1
    # Checks if Omari talks and will reply with a nice message
    elif msg.author.id == self.omariID and self.omariTalked != True:
      await msg.reply("Welcome back King")
      await msg.add_reaction("👑")
      self.omariTalked = True
    
    # Will always react to Omari's and I messages
    elif msg.author.id == self.omariID or msg.author.id == self.ZackId:
      await msg.add_reaction("👑")

    # Reaction for Sanita
    elif msg.author.id == self.sanitaID:
      await msg.add_reaction("🍓")

    # Reaction for Xavi
    elif msg.author.id == self.xaviID:
      await msg.add_reaction("🦙")
    
    # Reaction for Donal
    elif msg.author.id == self.donalID:
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
    





def setup(bot):
  bot.add_cog(functionality(bot))