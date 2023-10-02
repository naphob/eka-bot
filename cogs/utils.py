import discord
import discord.ui
from discord.ext import commands, pages

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="lineup", description="show team roster")
    async def lineup(self, ctx):
        embed = discord.Embed(
            title="TEAM ROSTER",
            color= discord.Color.from_rgb(255, 79, 0)
        )

        embed.add_field(name="LINE UP", value="`🔥 BackWiDowX\n🔥 Jiwjixz\n🔥 MYTG-\n🔥 Bizview`", inline=True)
        embed.add_field(name="COACH", value="`ZENZEEN`", inline=True)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1151145807769251950/1151146304093818880/EKA_logomark.png")

        await ctx.send(embed=embed)
        await ctx.send_response("แสดงผลแล้ว", ephemeral=True)

    @discord.slash_command(name="map", description="show team roster")
    async def map(self, ctx):
        file = discord.File('assets/EKA_MAP.png')
        await ctx.send(file=file)
        await ctx.send_response("แสดงผลแล้ว", ephemeral=True)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Utils(bot)) # add the cog to the bot
