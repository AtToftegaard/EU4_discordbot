# Work with Python 3.6
import discord, checkFile

TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXX'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!rolecreate'):
            author = message.author
        # split the string to get the rolename to create
            role_name = message.content.split("!rolecreate ", maxsplit=1)[1]
            role_name = role_name.title()
         # Checks the country codes file if the country exists, create the role.
            file = "country_codes.txt"
            if(checkFile.check_country(file, role_name)):
                    role = await client.create_role(author.server, name=role_name.capitalize(), colour=discord.Colour(0x0000FF))
                    await client.send_message(message.channel, role_name + " is now your country")
                    await client.add_roles(author, role)
            else:    
                await client.send_message(message.channel, role_name + " Does not exist in EU4")


    if message.content.startswith('!deleterole'):
        role_name = message.content.lower().split("!deleterole ", maxsplit=1)[1]
        role = discord.utils.get(message.server.roles, name=role_name)
        await client.delete_role(message.server, role)
 
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)