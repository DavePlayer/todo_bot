import discord

def readToken():
    with open('./token.txt', 'r') as f:
        return f.read()

client = discord.Client()

@client.event
async def on_message(message):
    print(message.content)
    if "BOT help" in message.content:
            await message.channel.send("GIMME HUGGIE WUGIES UWU")


client.run(readToken())