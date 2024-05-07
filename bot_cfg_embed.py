import discord
from discord import Streaming, Activity, ActivityType
from discord.ext import commands

import configparser
import logging
import json

# Basic Setup for the ConfigParser
config = configparser.ConfigParser()
config.read('.\config.cfg')
settings = config['DEFAULT']
channel_id = config['CHANNEL ID']

# Load language that is selected in the config file
language = settings['language']
with open(f'language/{language}.json', 'r', encoding='utf-8') as lang_file:
    lang = json.load(lang_file)

# Basic Setup for the Log File Writer
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8'
    )

# Intends settings for the Discord Library
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
#intents.presence = True

client = commands.Bot(command_prefix="!", intents=intents)

# Detect if the Bot is able to Log In with the given token
@client.event
async def on_ready():
    logging.info(f'We have logged in as {client.user}')
    print(f'We have logged in as {client.user}')

@client.event
async def on_voice_state_update(member, before, after):
    
    # ================ Create Embed Type Message ================
    def sendMsg(streamType, member, channel) -> discord.Embed:
        embed = discord.Embed(
            title=f""+streamType+" "+lang["stream_alert"]+" 』  📢", 
            description="", 
            color=0x3C87EA # Line Color of the Left Card
            ) 
        # Print Only the Username if Username and Nickname is the same
        if ("{}".format(member.nick) == "None"):
            embed.add_field(
                name=f"【 "+lang["user"]+" 】", 
                value="- {}".format(member), 
                inline=False
                )
        # Print Both if Username and Nickname is different
        else:
            embed.add_field(
                name=f"【 "+lang["user"]+" 】", 
                value="- {}".format(member.nick) + " ({})".format(member), 
                inline=False
                )
        # Print Channel Name
        embed.add_field(
            name=f"【 "+lang["channel"]+" 】", 
            value="- {}".format(channel), 
            inline=False
            )
        # Setup for the Thumbnali and Footer
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(
            text=lang["footer"],
            icon_url="http://webservice.dothome.co.kr/DiscordBotImg/labor_icon_256.png"
            )
        return embed
    
    if after.channel and after.channel.id == int(channel_id['voice']):
        
        # == Alert for Streaming ==
        if after.self_stream:
            alert_channel = discord.utils.get(
                member.guild.channels, 
                id=int(channel_id['alert'])
                )
            message = settings["mention_type"]+f' {member} has started streaming in {after.channel.name}'
            await alert_channel.send(message, delete_after=int(config['TIME']['delete_timeout']))
            logging.info(message)
            embedInstance = sendMsg("🖥️  『 "+lang["screen"], member, after.channel)
            await alert_channel.send("", embed=embedInstance, delete_after=int(config['TIME']['delete_timeout']))
        
        elif before.self_stream == True and after.self_stream == False:
            message = f'--------- {member} has ended streaming in {before.channel.name}'
            logging.info(message)

        # == Alert for Camera ==
        if after.self_video:
            alert_channel = discord.utils.get(
                member.guild.channels, 
                id=int(channel_id['alert'])
                )
            message = settings["mention_type"]+f' {member} has started camera in {after.channel.name}'
            await alert_channel.send(message, delete_after=int(config['TIME']['delete_timeout']))
            logging.info(message)
            embedInstance = sendMsg("📷  『 "+lang["camera"], member, after.channel)
            await alert_channel.send("", embed=embedInstance, delete_after=int(config['TIME']['delete_timeout']))
        
        elif before.self_video == True and after.self_video == False:
            message = f'---------- {member} has ended camera in {before.channel.name}'
            logging.info(message)

client.run(settings['token'])