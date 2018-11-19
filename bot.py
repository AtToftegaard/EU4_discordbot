## Work with Python 3.6
#import discord, checkFile, _commands
#from discord.ext import commands

TOKEN = 'NTEwODEzNjQ1MzUwMTA5MTg0.Dsh0Qg.mfYUuTpp8SuYC0bqijPfqqFbZu0'

##class eu4bot(commands.Bot):
##    def __init__(self):
##        self.command_prefix = '!'

#eu4bot = commands.Bot(command_prefix='!')

#@eu4bot.command()
#async def roll(dice : str):
#    """Rolls a dice in NdN format."""
#    try:
#        rolls, limit = map(int, dice.split('d'))
#    except Exception:
#        await bot.say('Format has to be in NdN!')
#        return

#    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#    await eu4bot.say(result)

#@eu4bot.event
#async def on_message(message):
#    # we do not want the bot to reply to itself (when would it?)
#    #if message.author == eu4bot.user:
#    #    return
#    eu4bot.process_commands(message)

#@eu4bot.event
#async def on_ready():
#    print('Logged in as')
#    print(eu4bot.user.name)
#    print(eu4bot.user.id)
#    print('------')

#eu4bot.run(TOKEN)

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await bot.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await bot.say(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await bot.say(random.choice(choices))

@bot.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await bot.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await bot.say('Yes, the bot is cool.')

bot.run(TOKEN)