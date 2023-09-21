import discord
import discord.ui
from discord.ext import commands, pages

class DGView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        button = discord.ui.Button(
                        label="รายละเอียดเพิ่มเติม",
                        style=discord.ButtonStyle.url,
                        url="https://www.facebook.com/DANGEROUS.ESPORTS.TH/posts/pfbid024XLTgALSMcjw3ERMToUPGm8QESoobcUEYVptEoWiCoQ8Dv1bvJ4ArVBxhLbUtUVul"
        )
        scoreboard = discord.ui.Button(
                        label="ตารางคะแนน",
                        style=discord.ButtonStyle.url,
                        url="https://twire.gg/en/pubg/tournaments/tournament/1143/dangerous-scrim-by-dangerous-esports/leaderboards?round=round128&group=group-8"
        )
        self.add_item(button)
        self.add_item(scoreboard)

    @discord.ui.button(label='', style=discord.ButtonStyle.gray, custom_id='notify1', emoji='🔕', disabled=True)
    async def notify_callback(self, button, interaction):
        await interaction.response.send_message("This tournament's alert has been set", ephemeral=True)

class PageView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        button2 = discord.ui.Button(
                        label="รายละเอียดเพิ่มเติม",
                        style=discord.ButtonStyle.url,
                        url="https://www.facebook.com/DANGEROUS.ESPORTS.TH/posts/pfbid037v2J5BMUkuHnyrCeZuxorJUCxUXek4BmNxCgj95TAwSEe71NV7xKWfZuCFfetYjAl"
        )
        scoreboard2 = discord.ui.Button(
                        label="ตารางคะแนน",
                        style=discord.ButtonStyle.url,
                        url="https://twire.gg/en/pubg/tournaments/tournament/1143/dangerous-scrim-by-dangerous-esports",
                        disabled=True
        )
        self.add_item(button2)
        self.add_item(scoreboard2)

    @discord.ui.button(label='', style=discord.ButtonStyle.blurple, custom_id='notify2', emoji='🔔')
    async def notify_callback(self, button, interaction):
        await interaction.response.send_message("This tournament's alert has been set", ephemeral=True)


class PTCView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        button = discord.ui.Button(
                        label="รายละเอียดเพิ่มเติม",
                        style=discord.ButtonStyle.url,
                        url="https://www.facebook.com/Attacker.Clan/posts/pfbid024fXVx8JS9Gj3wiVTufLHU7zQCqkWBCzibiTn8UTUtHMboikyzA9tvL5WEWVGRqJjl"
        )
        scoreboard = discord.ui.Button(
                        label="Scoreboard",
                        style=discord.ButtonStyle.url,
                        url="https://twire.gg/en/pubg/tournaments/tournament/1143/dangerous-scrim-by-dangerous-esports",
                        disabled=True
        )
        self.add_item(button)
        self.add_item(scoreboard)

    @discord.ui.button(label='', style=discord.ButtonStyle.blurple, custom_id='notify3', emoji='🔔')
    async def notify_callback(self, button, interaction):
        await interaction.response.send_message("This tournament's alert has been set", ephemeral=True)


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

    @discord.slash_command(name="map", description="show team roster")
    async def map(self, ctx):
        file = discord.File('assets/EKA_MAP.png')
        await ctx.send(file=file)
        await ctx.send_response("แสดงผลแล้ว", ephemeral=True)

    @discord.slash_command(name="tournaments", description="show upcoming tournament")
    async def tournaments(self, ctx: discord.ApplicationContext):
        tour_page = []
        embed = discord.Embed(
            title="ANGEROUS TOURNAMENT BY AFREECATV SS2",
            color=discord.Color.from_rgb(255, 79, 0)
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1106995464852738140/1134885054481444885/received_152468377868777.webp")
        embed.add_field(name="Roud", value="`128 ทีม`")
        embed.add_field(name="Group", value="`8`")
        embed.add_field(name="Status", value="`End`")
        embed.add_field(name="Result", value="`อันดับ 8`")
        embed.add_field(name="Time", value="`21/09/2023 20:40`")

        embed2 = discord.Embed(
            title="ANGEROUS TOURNAMENT BY AFREECATV SS2",
            color=discord.Color.from_rgb(255, 79, 0)
        )
        embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/1106995464852738140/1134885054481444885/received_152468377868777.webp")
        embed2.add_field(name="Roud", value="`64 ทีม`")
        embed2.add_field(name="Group", value="`3`")
        embed2.add_field(name="Status", value="`UPCOMING`")
        embed2.add_field(name="Result", value="`-`")
        embed2.add_field(name="Time", value="`22/09/2023 19:00`")

        embed3 = discord.Embed(
            title="PUBG Thailand Championship 2023",
            color=discord.Color.from_rgb(255, 79, 0)
        )

        embed3.set_thumbnail(url="https://twire-assets.s3.eu-west-1.amazonaws.com/pubg/tournament-logos/ptc-23.png")
        embed3.set_image(url="https://lh5.googleusercontent.com/1rrt7rQidfMyBu72rdvM6AyZ9v5tWo9lro1yzsP0AiKXkLZPLCZ_mAuXU9ou7Lxi4alw2jxCRcyaqMpau4HeNk0PurSaDiCm0BP8wTDkG1YSwITBlAUa6uHlzZb6rGjd6Q=w1600")
        embed3.add_field(name="Roud", value="`-`")
        embed3.add_field(name="Group",value="`-`")
        embed3.add_field(name="Status",value="`UPCOMING`")
        embed3.add_field(name="Result",value="`-`")
        embed3.add_field(name="Time", value="`28/09/2023`")



        page = pages.Page(
            embeds=[embed],
            custom_view=DGView()
        )

        page2 = pages.Page(
            embeds=[embed2],
            custom_view=PageView()
        )

        page3 = pages.Page(
            embeds=[embed3],
            custom_view=PTCView()
        )


        tour_page.append(page)
        tour_page.append(page2)
        tour_page.append(page3)

        paginator = pages.Paginator(pages=tour_page, loop_pages= True, timeout=None)
        paginator.remove_button("first")
        paginator.remove_button("last")

        await paginator.respond(ctx.interaction, ephemeral=False)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Utils(bot)) # add the cog to the bot
