import discord
from exams.exams import ExamsArray
from datetime import date
from exams.getDayName import getDayName

# created file with one line which contains token of the bot
def readToken():
    with open('./token.txt', 'r') as f:
        return f.read()

def getSerwerId():
    with open ('./serwer.txt', 'r') as f:
        return int(f.read())

client = discord.Client()
exams = ExamsArray()

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
                exams.addExam(str(data[0]), str(data[1]), str(data[2]), examType=str(data[3]))
        if "BOT display" in message.content:
            for exam in exams.exams:
                await message.channel.send(f"{exam.day}.{exam.month} {getDayName(date(2020, int(exam.month), int(exam.day)).weekday())} {exam.subject} -- {exam.examType}")


client.run(readToken())