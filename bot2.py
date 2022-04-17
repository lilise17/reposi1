from argparse import ArgumentParser
from email.policy import default
from discord.ext import commands
import discord 
import logging 
import json

with open('configbot2.json') as json_data:
        data_dict = json.load(json_data)

        
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"{self.user.display_name} est prêt !")


    async def on_message(self, message):
        logging.basicConfig(filename=data_dict.get("nom du fichier log"),encoding='utf-8',
        level=logging.WARNING,format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        if message.content=="!coucou":
            await message.channel.send("Hello !")
            logging.warning('is when !coucou is written')
        if message.content=="!help":
            await message.channel.send("Les commandes utilisables sont: !help, !coucou, !ping")
            logging.warning('is when !help is written')
        if message.content=="!ping":
            await message.channel.send("pong !")
            logging.warning('is when !ping is written')


    async def parge_args():
       parser = ArgumentParser()
       parser.add_argument("-c","--config",help="Config file",required=True,dest="configbot2")
       return parser.parse_args()


client=MyBot()
client.run(data_dict.get("token"))

