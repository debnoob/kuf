import discord
import os 
client = discord.Client()
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('emf'):   
        await message.channel.send(file=discord.File('Screenshot from 2021-02-04 08-51-42.png'))
                                                  

client.run('token')
