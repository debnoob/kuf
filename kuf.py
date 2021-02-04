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
        await message.channel.send(file=discord.File('Screenshot from 2020-10-04 17-06-59.png'))
    if message.content.startswith('wheatstone bridge'):   
        await message.channel.send(file=discord.File('Screenshot from 2020-10-05 05-04-47.png'))
    
    if message.content.startswith('application derivatives'):   
        await message.channel.send(file=discord.File('Screenshot from 2020-10-05 12-43-59.png','Screenshot from 2020-10-05 12-49-39.png'))
    if message.content.startswith('derivative of cos(x+y)'):   
        await message.channel.send(file=discord.File('Screenshot from 2020-10-05 14-32-40.png'))
    if message.content.startswith('newman and horse'):   
        await message.channel.send(file=discord.File('Screenshot from 2020-10-05 17-13-50.png'))   
    if message.content.startswith('nomenclature'):
       await message.channel.send(file=discord.File('Screenshot from 2020-10-05 17-13-50.png'))
             
    if message.content.startswith('alkene preparation with alkynes'):   
       await message.channel.send(file=discord.File('Screenshot from 2020-10-06 10-28-00.png'))
    if message.content.startswith('kolbe reaction'):
       await message.channel.send(file=discord.File('Screenshot from 2020-10-06 10-33-56.png'))
    if message.content.startswith('phase angle'):
       await message.channel.send(file=discord.File('Screenshot from 2020-10-06 16-37-18.png'))   
    if message.content.startswith('wave optics fi'):
       await message.channel.send(file=discord.File('Screenshot from 2020-10-06 16-34-45.png'))                                                   

client.run(os.environ['token'])
