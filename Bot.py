import os
from discord.ext.commands import Bot
from discord.utils import find
from dotenv import load_dotenv
import asyncio
import discord
import random
client = Bot(command_prefix = '#') 
async def sick_beats_bro():
    music = [
        "https://www.youtube.com/watch?v=zW0Gn2ZV6Ys",
        "https://www.youtube.com/watch?v=Zy6hbtm3hrI",
        "https://www.youtube.com/watch?v=Ya8Sng3mZqA",
        "https://www.youtube.com/watch?v=7_6gFfyibhE",
        "https://www.youtube.com/watch?v=iFToc0inaeE",
        "https://www.youtube.com/watch?v=MQurUl4Snio"
    ]
    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{random.choice(music)} | (#help)"))
        await asyncio.sleep(60 * 120) # because I'm too lazy to do the math rn
@client.event
async def on_ready():
    client.loop.create_task(sick_beats_bro())
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error! <:ImgShareError:851852314242973746> did you fill out everything correctly? (Error Message: {str(error)})")
    print(str(error))

@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Guidelines: \n No NSFW \n No Deepfakes (looking at you <@729135459405529118> <:eyes_sus:851168417453047808>) \n No Racisim \n If you wouldnt show your friends/family it, dont post it (eg: dont post anything offensive)'.format(guild.name))
client.load_extension('image_sharing')
load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))