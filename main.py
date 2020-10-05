import discord
import schedule
import asyncio
from examSystem.exams import ExamsArray
from datetime import date, datetime, time
from examSystem.getDayName import getDayName


client = discord.Client()
exams = ExamsArray()

# created file with one line which contains token of the bot
def readToken():
    with open('./token.txt', 'r') as f:
        return f.read()

def getSerwerId():
    with open ('./serwer.txt', 'r') as f:
        return int(f.read())

async def daily_task():
    print("bot fully loaded")
    print('reseting days at sundays 7:00. Current hour: ', datetime.now().hour)
    if int(date.today().weekday()) == 7 and int(datetime.now().hour) == 7:
        exams.resetExams()
    await asyncio.sleep(60*60)

@client.event
async def on_ready():
    await daily_task()

@client.event
async def on_message(message):
    # serwerId = client.get_guild(getSerwerId())

    if str(message.channel) in ["todo"]:
        if "BOT help" in message.content:
                embed = discord.Embed(title = "Help commands", description = "I'm vewy sowwy about your wack of nowledge ;;W;; \n I am hona solwe youu pwobwem UWU")
                embed.add_field(name = "BOT help", value="Displays helpful commands. \n Only idiot wouldn't know that")
                embed.add_field(name = "BOT display", value="Displays current week exams in JSON format")
                embed.add_field(name = "BOT add <numer dnia kalendarzowego> <numer miesiąca> <nazwa przedmiotu> <typ sprawdzianu>", value="adds new records by date parsed to command. \nEvery sunday at 23:00  records with date over this week wil be removed")
                embed.add_field(name = "BOT remove <numer dnia kalendażowego> <numer miesiąca> <nazwa przedmiotu>", value="removes record by date and name of subject parsed to command.")
                await message.channel.send(content=None, embed = embed)
        if "BOT add" in message.content:
                data = message.content.split()
                data.pop(0)
                data.pop(0)
                if ( int(data[0]) >= int(date.today().day) and int(date.today().month) == int(data[1]) ) or ( int(data[1]) > int(date.today().month) ) or ( int(date.today().month) == 12 ):
                    if int(date.today().month) == 12 and int(data[1]) != 12:
                        exams.addExam(str(data[0]), str(data[1]), date.today().year + 1 , str(data[2]), examType=str(data[3]))
                        await message.channel.send(" ``` Dodawanie sprawdzianu zakończone na następny rok  ``` ")
                    else:
                        exams.addExam(str(data[0]), str(data[1]), date.today().year , str(data[2]), examType=str(data[3]))
                        await message.channel.send(" ``` Dodawanie sprawdzianu zakończone na ten rok  ``` ")
                else:
                    await message.channel.send(" ``` Nie można dodawać zaległych sprawdzianów  ``` ")
        if "BOT display" in message.content:
            # today = date.today().day
            # await message.channel.send(today)
            if len(exams.exams) > 0:
                for exam in exams.exams:
                    await message.channel.send(f"{exam.day}.{exam.month} {getDayName(date(2020, int(exam.month), int(exam.day)).weekday())} {exam.subject} -- {exam.examType}")
            else:
                await message.channel.send("Nie ma żadnych rekordów")

client.run(readToken())
schedule.every().sunday.at("10:00").do(exams.resetExams())

# i = 0
# for exam in exams.exams:
#     # beggining = int(date.today().day) - int(date.today().weekday())
#     # print('week beggining date: ', beggining)
#     # # if(beggining < 0) :
#     # #     beggining = int(date(date.today().year, int(exam.month) -1, ))egg
#     # print( datetime.now() - timedelta(days=beggining))
#     # print( datetime(date.today().year, int(exam.month), int(exam.day)) > datetime(2020, 10, 7) )

#     if i < 5:
#         print(f'(readToken({exam.day}.{exam.month} {getDayName(date(date.today().year, int(exam.month), int(exam.day)).weekday())} {exam.subject} -- {exam.examType}')
#         i += 1

# exams.resetExams()
    