import asyncio
import re
import random
import discord
import enchant
from datetime import date

client = discord.Client()
weekNumber = date.today().weekday

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')

client.run('NDU4MTkyMTkwMzAxMDExOTc1.DgkF5g.aXxnMI3ZWWf9N3CP2KoXqEcZeh0')