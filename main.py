# This example requires the 'message_content' intent.

import discord
import os

from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

party = []

load_dotenv("environments\discordKeys.env")
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s) ")
    except Exception as e :
        print(e)

@bot.tree.command(name="go")
async def goDota2(interaction:discord.Interaction):
    party.append({"name":interaction.user.name,"id":interaction.user.id})
    print(f"userid - {interaction.user.id}")
    print(party)
    await interaction.response.send_message(f"{interaction.user.mention} esta listo para rankear\n")

bot.run(TOKEN)