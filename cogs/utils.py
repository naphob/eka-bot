import discord
import discord.ui
from discord.ext import commands, pages

class PaginatorView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

class DGView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        button = discord.ui.Button(label="รายละเอียดเพิ่มเติม", style=discord.ButtonStyle.url, url="https://www.facebook.com/DANGEROUS.ESPORTS.TH/posts/pfbid024XLTgALSMcjw3ERMToUPGm8QESoobcUEYVptEoWiCoQ8Dv1bvJ4ArVBxhLbUtUVul")
        self.add_item(button)

class PTCView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        button = discord.ui.Button(label="รายละเอียดเพิ่มเติม", style=discord.ButtonStyle.url, url="https://www.facebook.com/Attacker.Clan/posts/pfbid024fXVx8JS9Gj3wiVTufLHU7zQCqkWBCzibiTn8UTUtHMboikyzA9tvL5WEWVGRqJjl")
        self.add_item(button)

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="lineup", description="show team roster")
    async def lineup(self, ctx):
        embed = discord.Embed(
            title="TEAM ROSTER",
            color= discord.Color.from_rgb(255, 79, 0)
        )

        embed.add_field(name="LINE UP", value="`- BackwidowX\n- Jiwjix\n- MYTG-\n- Bizview`", inline=True)
        embed.add_field(name="COACH", value="`ZENZEEN`", inline=True)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1151145807769251950/1151146304093818880/EKA_logomark.png")

        await ctx.send(embed=embed)
        await ctx.send_response("แสดงผลแล้ว", ephemeral=True)

    @discord.slash_command(name="dropmap", description="show team roster")
    async def dropmap(self, ctx):
        file = discord.File('assets/EKA_MAP.png')
        await ctx.send(file=file)
        await ctx.send_response("แสดงผลแล้ว", ephemeral=True)

    @discord.slash_command(name="tour", description="show upcoming tournament")
    async def tour(self, ctx: discord.ApplicationContext):
        tour_page = []
        embed = discord.Embed(
            title="ANGEROUS TOURNAMENT BY AFREECATV SS2",
            color=discord.Color.dark_red()
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1106995464852738140/1134885054481444885/received_152468377868777.webp")
        embed.add_field(name="รอบคัดเลือก 128 ทีม",value="`21/09/2023 20:40`")
        embed.add_field(name="Group",value="`8`")
        embed.add_field(name="Status",value="`UPCOMING`")
        embed.add_field(name="Result",value="`-`")

        embed2 = discord.Embed(
            title="PUBG Thailand Championship 2023",
            color=discord.Color.dark_red()
        )
        embed2.set_thumbnail(url="https://twire-assets.s3.eu-west-1.amazonaws.com/pubg/tournament-logos/ptc-23.png")
        embed2.set_image(url="https://lh5.googleusercontent.com/1rrt7rQidfMyBu72rdvM6AyZ9v5tWo9lro1yzsP0AiKXkLZPLCZ_mAuXU9ou7Lxi4alw2jxCRcyaqMpau4HeNk0PurSaDiCm0BP8wTDkG1YSwITBlAUa6uHlzZb6rGjd6Q=w1600")
        embed2.add_field(name="รอบคัดเลือก",value="`28/09/2023`")
        embed2.add_field(name="Group",value="`-`")
        embed2.add_field(name="Status",value="`UPCOMING`")
        embed2.add_field(name="Result",value="`-`")

        page = pages.Page(
            embeds=[embed],
            custom_view=DGView()
        )

        page2 = pages.Page(
            embeds=[embed2],
            custom_view=PTCView()
        )


        tour_page.append(page)
        tour_page.append(page2)

        paginator = pages.Paginator(pages=tour_page, loop_pages= True)
        paginator.remove_button("first")
        paginator.remove_button("last")

        await paginator.respond(ctx.interaction, ephemeral=False)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Utils(bot)) # add the cog to the bot
