import discord
import scrapper
from discord.ext import commands
import os
import csv
from io import StringIO

from dotenv import load_dotenv
load_dotenv()



TOKEN= os.getenv("BOT_TOKEN")
if TOKEN:
    print(f"BOT_TOKEN: {TOKEN}")
else:
    print("BOT_TOKEN not found. Make sure it's defined in your .env file.")


def generate_csv_from_string(csv_string):
    csv_output = StringIO()
    csv_output.write(csv_string)
    csv_output.seek(0)
    return discord.File(csv_output, filename='generated.csv')

async def send_message(message,user_message,gen,is_private):
    try:
        if gen:
            response = scrapper.get_response(user_message)
            if response:
        
                csv_file = generate_csv_from_string(response)

        
                await message.channel.send('Here is the CSV file:', file=csv_file) 
            else:
                await message.author.send('No data to generate the CSV file.')
        else:
            response = scrapper.get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
    
def run_discord_bot():
    intents=discord.Intents.default()
    intents.message_content = True
    client=discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username=str(message.author)
        user_message =str(message.content)
        channel=str(message.channel)
        gen=False
        if user_message=='/generate':
            gen=True
        print(f'{username} said: "{user_message}" ({channel})')



        if user_message[0]=='?':
            user_message =user_message[1:]
            await send_message(message,user_message,gen,is_private=True)
        else:
            await send_message(message,user_message,gen,is_private=False)

    client.run(TOKEN)

run_discord_bot()



# env start: source /home/priyanshu/Desktop/hola/task-06/bot-env/bin/activate