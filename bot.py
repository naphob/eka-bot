import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from rich.console import Console
from cogs.utils import DGView, PTCView

console = Console()
load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(intents=intents)
cogs_list = [
    'welcomes',
    'announces',
    'utils',
]

@bot.event
async def on_ready():
        console.log(f'{bot.user.name} has connected to Discord!')

        bot.add_view(DGView())
        bot.add_view(PTCView())

        for guild in bot.guilds:
            # PRINT THE SERVER'S ID AND NAME.
            console.log(f"- {guild.id} | {guild.name}")

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(TOKEN)
