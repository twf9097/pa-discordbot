import discord
from discord.ext import commands
from quotes import Quotes
client = commands.Bot(command_prefix="*")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

client.add_cog(Quotes(client))