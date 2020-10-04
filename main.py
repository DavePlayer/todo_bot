import discord

# created file with one line which contains token of the bot
def readToken():
    with open('./token.txt', 'r') as f:
        return f.read()

def getSerwerId():
    with open ('./serwer.txt', 'r') as f:
        return int(f.read())

client = discord.Client()

@client.event
async def on_message(message):
    # serwerId = client.get_guild(getSerwerId())

    if str(message.channel) in ["todo"]:
        if "BOT help" in message.content:
                embed = discord.Embed(title = "Help commands", description = "I'm vewy sowwy about your wack of nowledge ;;W;; \n I am hona solwe youu pwobwem UWU")
                embed.add_field(name = "BOT help", value="Displays helpful commands. \n Only idiot wouldn't know that")
                embed.add_field(name = "BOT display", value="Displays current week exams in JSON format")
                embed.add_field(name = "BOT add <numer dnia kalendażowego> <numer miesiąca> <nazwa przedmiotu> <typ sprawdzianu>", value="adds new records by date parsed to command. \nEvery sunday at 23:00  records with date over this week wil be removed")
                embed.add_field(name = "BOT remove <numer dnia kalendażowego> <numer miesiąca> <nazwa przedmiotu>", value="removes record by date and name of subject parsed to command.")
                await message.channel.send(content=None, embed = embed)
        if "BOT add" in message.content:
                data = message.content.split()
                data.pop(0)
                data.pop(0)
                print(data)


client.run(readToken())