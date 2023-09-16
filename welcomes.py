import os
import re
import discord
import discord.ui
from discord.ext import commands
from dotenv import load_dotenv
from rich.console import Console
from PIL import Image, ImageFont, ImageDraw

console = Console()
load_dotenv()

WELCOME_CHANNEL_ID = 1151150503032524803

class Welcomes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def welcome_pic(self, user):
        channel = await self.bot.fetch_channel(WELCOME_CHANNEL_ID)
        await user.display_avatar.save('Asset/avatar.png')
        avatar = Image.open('Asset/avatar.png')
        count = user.guild.member_count
        username = user.name
        text = f"Welcome {username} to IDS"
        member_text = f"Member #{count}"
        img =Image.open("Asset/ids_bg.png")
        W, H = img.size
        avatar = Image.open("Asset/avatar.png")
        size = (240, 240)
        avatar = avatar.resize(size, Image.Resampling.LANCZOS)
        mask_img = Image.new("L", avatar.size, 0)
        mask_draw = ImageDraw.Draw(mask_img)
        mask_draw.ellipse((0, 0) + avatar.size, fill=255)
        mask_img.save("assets/mask_circle.jpg", quality=95)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 50)
        count_font = ImageFont.truetype("arial.ttf", 32)

        img.paste(avatar ,(440, 80), mask_img)
        text_size =draw.textlength(text, font=font)
        count_size =draw.textlength(member_text, font=count_font)
        draw.text(((W-text_size)/ 2, 340), text, fill=(255, 255, 255, 255), font=font, aligh="center")
        draw.text(((W-count_size)/ 2, 400), member_text, fill="grey", font=count_font, aligh="center")
        img.save('assets/text.png')

        await channel.send(file= discord.File('Asset/text.png'))

    @commands.Cog.listener()
    async def on_member_join(self, member):
        role = 1045127837989994568 #give new_face role to new joiner so they can see welcome chanel
        await member.add_roles(member.guild.get_role(role))
        await self.welcome_pic(member)

    @discord.slash_command(name="welcome", description="Welcome new member")
    async def welcome(self,ctx, user: discord.Member):
        await self.welcome_pic(user)

    @discord.slash_command(name="role", description="Select a role")
    async def role(self, ctx):
        embed = discord.Embed(
                title = "Welcome to the verse",
                description=f"เลือก Role ที่เหมาะสมกับคุณ เพื่อใช้ในการสื่อสารภายในดิสคอร์ด",
                color=discord.Color.dark_purple()
            )

        await ctx.respond(embed=embed, view=GetRoles())

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Welcomes(bot)) # add the cog to the bot
