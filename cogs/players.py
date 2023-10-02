import discord
import discord.ui
from firebase_admin import db
from discord.ext import commands, pages
from firebase.firebase import *

class PlayerModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, timeout=None)

        self.players = db.reference('players')
        self.add_item(discord.ui.InputText(label="IGN", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Player ID", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="Role", style=discord.InputTextStyle.short, required=False))

    async def callback(self, interaction: discord.Interaction):
        ign = self.children[0].value
        player_id = self.children[1].value
        role = self.children[2].value

        self.players.child(f"{player_id}").update({
            'ign': ign,
            'role': role,
        })
        await interaction.response.send_message(f"สร้างข้อมูลแล้ว", ephemeral=True)

class Players(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.players = db.reference('players')

    @discord.slash_command(name="players_add", description="Add new tournament")
    @commands.has_any_role(1152643171801636924)
    async def players_add(self, ctx: discord.ApplicationContext):
        modal = PlayerModal(title="New Player")
        await ctx.send_modal(modal)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Players(bot)) # add the cog to the bot
