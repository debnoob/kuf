import discord
import os 
client = discord.Client()
token="NzMzNjA5MTcyOTY4NjY5MzA0.XxFoyA.4_qp5np1kR7CZh3DgehxCZVBt9M"
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('emf'):   
        await message.channel.send(file=discord.File('Screenshot from 2021-02-04 08-51-42.png'))
                                                  

client.run(token)
