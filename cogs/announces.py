import discord
import discord.ui
from discord.ext import commands
from rich.console import Console
console = Console()

class AnnouceModal(discord.ui.Modal):
    def __init__(self, bot, channel:discord.TextChannel, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, timeout=None)
        self.bot = bot
        self.channel = channel

        self.add_item(discord.ui.InputText(label="หัวข้อ", style=discord.InputTextStyle.short))
        self.add_item(discord.ui.InputText(label="รายละเอียดหัวข้อ", style=discord.InputTextStyle.short, required=False))
        self.add_item(discord.ui.InputText(label="เนื้อหา", style=discord.InputTextStyle.long))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
                    title="ประกาศ",
                    description= self.children[1].value,
                    color= discord.Color.from_rgb(255, 79, 0)
        )
        embed.add_field(name=self.children[0].value, value=self.children[2].value)

        await self.channel.send(embed=embed)
        await interaction.response.send_message(f"ส่งประกาศไปที่ {self.channel} แล้ว", ephemeral = True)

class Announces(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="annouce", description="make an annoucement")
    @commands.has_any_role(1152643171801636924)
    async def announce(self, ctx, channel:discord.TextChannel):
        modal = AnnouceModal(self.bot, channel, title="ประกาศ")
        await ctx.send_modal(modal)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Announces(bot)) # add the cog to the bot
