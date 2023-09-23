import uuid
import discord
import discord.ui
from firebase_admin import db
from discord.ext import commands, pages
from firebase.firebase import *

# class DGView(discord.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#         button = discord.ui.Button(
#                         label="รายละเอียดเพิ่มเติม",
#                         style=discord.ButtonStyle.url,
#                         url="https://www.facebook.com/DANGEROUS.ESPORTS.TH/posts/pfbid024XLTgALSMcjw3ERMToUPGm8QESoobcUEYVptEoWiCoQ8Dv1bvJ4ArVBxhLbUtUVul"
#         )
#         scoreboard = discord.ui.Button(
#                         label="ตารางคะแนน",
#                         style=discord.ButtonStyle.url,
#                         url="https://twire.gg/en/pubg/tournaments/tournament/1143/dangerous-scrim-by-dangerous-esports/leaderboards?round=round128&group=group-8"
#         )
#         self.add_item(button)
#         self.add_item(scoreboard)

#     @discord.ui.button(label='', style=discord.ButtonStyle.gray, custom_id='notify1', emoji='🔕', disabled=True)
#     async def notify_callback(self, button, interaction):
#         await interaction.response.send_message("This tournament's alert has been set", ephemeral=True)

class UpdateView(discord.ui.View):
    def __init__(self, id):
        super().__init__(timeout=None)
        self.tournaments = db.reference('tournaments')
        self.id = id

    @discord.ui.button(label='Update Info', style=discord.ButtonStyle.blurple, custom_id='notify3')
    async def update_callback(self, button, interaction):
        modal = UpdateModal(self.id, title="Update Tournament Info")
        await interaction.response.send_modal(modal)

class TournamentModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, timeout=None)

        self.tournaments = db.reference('tournaments')

        self.add_item(discord.ui.InputText(label="Title", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Logo URL", style=discord.InputTextStyle.short, required=False))
        self.add_item(discord.ui.InputText(label="Banner URL", style=discord.InputTextStyle.short, required=False))
        self.add_item(discord.ui.InputText(label="Detail URL", style=discord.InputTextStyle.short, required=False))
        self.add_item(discord.ui.InputText(label="Scoreboard URL", style=discord.InputTextStyle.short, required=False))

    async def callback(self, interaction: discord.Interaction):
        tournament_id = uuid.uuid4()
        title = self.children[0].value
        logo = self.children[1].value
        detail = self.children[2].value
        score = self.children[3].value

        self.tournaments.child(f"{tournament_id}").update({
            'title': title,
            'logo': logo,
            'detail': detail,
            'score': score,
            'status': 'UPCOMING'
        })
        await interaction.response.send_message(f"สร้างข้อมูลแล้ว", ephemeral=True)

class UpdateModal(discord.ui.Modal):
    def __init__(self, id, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, timeout=None)

        self.tournaments = db.reference('tournaments')
        self.id = id

        self.add_item(discord.ui.InputText(
                                        label="Round",
                                        style=discord.InputTextStyle.short,
                                        required=False,
                                        value=self.tournaments.child(f"{id}").child('round').get()
                                    ))
        self.add_item(discord.ui.InputText(label="Group",
                                        style=discord.InputTextStyle.short,
                                        required=False,
                                        value=self.tournaments.child(f"{id}").child('group').get()
                                    ))
        self.add_item(discord.ui.InputText(label="Status",
                                        style=discord.InputTextStyle.short,
                                        required=False,
                                        value=self.tournaments.child(f"{id}").child('status').get()
                                    ))
        self.add_item(discord.ui.InputText(label="Result",
                                        style=discord.InputTextStyle.short,
                                        required=False,
                                        value=self.tournaments.child(f"{id}").child('result').get()
                                    ))
        self.add_item(discord.ui.InputText(label="Date",
                                        style=discord.InputTextStyle.short,
                                        required=False,
                                        value=self.tournaments.child(f"{id}").child('date').get()
                                    ))

    async def callback(self, interaction: discord.Interaction):
        tournament_id = self.id
        round = self.children[0].value
        group = self.children[1].value
        status = self.children[2].value
        result = self.children[3].value
        date = self.children[4].value

        self.tournaments.child(f"{tournament_id}").update({
            'round': round,
            'group': group,
            'status': status,
            'result': result,
            'date': date
        })
        await interaction.response.send_message(f"อัพเดตข้อมูลแล้ว", ephemeral=True)

class Tournaments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tournaments = db.reference('tournaments')

    @discord.slash_command(name="tournaments", description="show tournament pages")
    async def tournaments(self, ctx: discord.ApplicationContext):
        tournaments = self.tournaments.get()
        tournaments_pages = []
        for id in tournaments:

            logo = self.tournaments.child(f"{id}").child('logo').get()
            banner = self.tournaments.child(f"{id}").child('banner').get()
            round = self.tournaments.child(f"{id}").child('round').get()
            group = self.tournaments.child(f"{id}").child('group').get()
            status = self.tournaments.child(f"{id}").child('status').get()
            result = self.tournaments.child(f"{id}").child('result').get()
            date = self.tournaments.child(f"{id}").child('date').get()

            embed = discord.Embed(
                title=self.tournaments.child(f"{id}").child('title').get(),
                color=discord.Color.from_rgb(255, 79, 0)
            )

            if logo is not None:
                embed.set_thumbnail(url=logo)

            if  banner is not None:
                embed.set_image(url=banner)

            if round is not None:
                embed.add_field(name="Round", value=f"`{round}`")
            else:
                embed.add_field(name="Round", value="`-`")

            if group is not None:
                embed.add_field(name="Group", value=f"`{group}`")
            else:
                embed.add_field(name="Group", value="`-`")

            if status is not None:
                embed.add_field(name="Status", value=f"`{status}`")
            else:
                embed.add_field(name="Status", value="`-`")

            if result is not None:
                embed.add_field(name="Result", value=f"`{result}`")
            else:
                embed.add_field(name="Result", value="`-`")

            if date is not None:
                embed.add_field(name="Date", value=f"`{date}`")
            else:
                embed.add_field(name="Date", value="`-`")

            page = pages.Page(
            embeds=[embed]
            )

            tournaments_pages.append(page)
        paginator = pages.Paginator(pages=tournaments_pages, loop_pages= True, timeout=None)
        paginator.remove_button("first")
        paginator.remove_button("last")

        await paginator.respond(ctx.interaction)

    @discord.slash_command(name="tournaments_add", description="Add new tournament")
    @commands.has_any_role(1152643171801636924)
    async def tournaments_add(self, ctx: discord.ApplicationContext):
        modal = TournamentModal(title="New Tournament")
        await ctx.send_modal(modal)

    @discord.slash_command(name="tournaments_admin", description="Manage tournament")
    @commands.has_any_role(1152643171801636924)
    async def tournaments_admin(self, ctx: discord.ApplicationContext):
        tournaments = self.tournaments.get()
        tournaments_pages = []
        for id in tournaments:

            logo = self.tournaments.child(f"{id}").child('logo').get()
            banner = self.tournaments.child(f"{id}").child('banner').get()
            round = self.tournaments.child(f"{id}").child('round').get()
            group = self.tournaments.child(f"{id}").child('group').get()
            status = self.tournaments.child(f"{id}").child('status').get()
            result = self.tournaments.child(f"{id}").child('result').get()
            date = self.tournaments.child(f"{id}").child('date').get()

            embed = discord.Embed(
                title=self.tournaments.child(f"{id}").child('title').get(),
                color=discord.Color.from_rgb(255, 79, 0)
            )

            if logo is not None:
                embed.set_thumbnail(url=logo)

            if  banner is not None:
                embed.set_image(url=banner)

            if round is not None:
                embed.add_field(name="Round", value=f"`{round}`")
            else:
                embed.add_field(name="Round", value="`-`")

            if group is not None:
                embed.add_field(name="Group", value=f"`{group}`")
            else:
                embed.add_field(name="Group", value="`-`")

            if status is not None:
                embed.add_field(name="Status", value=f"`{status}`")
            else:
                embed.add_field(name="Status", value="`-`")

            if result is not None:
                embed.add_field(name="Result", value=f"`{result}`")
            else:
                embed.add_field(name="Result", value="`-`")

            if date is not None:
                embed.add_field(name="Date", value=f"`{date}`")
            else:
                embed.add_field(name="Date", value="`-`")

            page = pages.Page(
            embeds=[embed],
            custom_view=UpdateView(id)
            )

            tournaments_pages.append(page)
        paginator = pages.Paginator(pages=tournaments_pages, loop_pages= True, timeout=None)
        paginator.remove_button("first")
        paginator.remove_button("last")

        await paginator.respond(ctx.interaction)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Tournaments(bot)) # add the cog to the bot
