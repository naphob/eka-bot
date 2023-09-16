import os
import re
import discord
import discord.ui
from discord.ext import commands
from dotenv import load_dotenv
from rich.console import Console
from PIL import Image, ImageFont, ImageDraw, ImageOps

console = Console()
load_dotenv()

WELCOME_CHANNEL_ID = 1151150503032524803

class Welcomes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def welcome_pic(self, user):
        channel = await self.bot.fetch_channel(WELCOME_CHANNEL_ID)
        await user.display_avatar.save('assets/avatar.png')
        avatar = Image.open('assets/avatar.png')
        avatar = avatar.convert("RGBA")
        avatar.save('assets/avatar.png')
        avatar = Image.open('assets/avatar.png')
        username = user.name
        text = f"WELCOME {username.upper()}"
        img =Image.open("assets/welcome_bg.png")
        W, H = img.size
        avatar = Image.open("assets/avatar.png")
        size = (240, 240)
        avatar = avatar.resize(size, Image.Resampling.LANCZOS)
        mask_img = Image.new("L", avatar.size, 0)
        mask_draw = ImageDraw.Draw(mask_img)
        mask_draw.ellipse((0, 0) + avatar.size, fill=255)

        avatar = ImageOps.fit(avatar, mask_img.size, centering=(0.5, 0.5))
        avatar.putalpha(mask_img)

        avatar = avatar.convert("RGBA")
        img = img.convert("RGBA")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("fonts/POPPINS-BLACK.TTF", 50)
        img.paste(avatar, (440, 80), avatar)
        text_size = draw.textlength(text, font=font)
        draw.text(((W-text_size)/ 2, 340), text, fill=(255, 255, 255, 255), font=font, aligh="center")
        img.save('assets/output.png')

        await channel.send(file= discord.File('assets/output.png'))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = 1045127837989994568 #give new_face role to new joiner so they can see welcome chanel
        await self.welcome_pic(member)

    @discord.slash_command(name="welcome", description="Welcome new member")
    async def welcome(self,ctx, user: discord.Member):
        await self.welcome_pic(user)
        await ctx.send_response("Welcome image has been posted.", ephemeral=True)


def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Welcomes(bot)) # add the cog to the bot
