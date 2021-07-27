import asyncio
import os
import discord
from pathlib import Path
from discord.ext.commands import Bot
from discord.utils import find
from dotenv import load_dotenv
from pretty_help import DefaultMenu, PrettyHelp
from discord import Color

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

client = Bot(command_prefix = '#') 

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error! <:ImgShareError:851852314242973746> did you fill out everything correctly? (Error Message: {str(error)})")
    print(str(error))
@client.event
async def on_ready():
    client.loop.create_task(status_task())

client.load_extension("cogs.get")
client.load_extension("cogs.other")
client.load_extension("cogs.post")
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(name="Yo Mama: The Game | (#help)"))
        await asyncio.sleep(60)
        await client.change_presence(activity=discord.Game(name="Hey Pikmin 2 | (#help)"))
        await asyncio.sleep(60)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="The end of the world | (#help)"))
        await asyncio.sleep(60)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Lo-fi Hip-Hop Beats To Treat Patients To | (#help)"))
        await asyncio.sleep(60)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="People whine about the logo like babies :trol: | (#help)"))
        await asyncio.sleep(60)
@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Guidelines: \n No NSFW \n No Deepfakes (looking at you <@729135459405529118> <:eyes_sus:851168417453047808>) \n No Racisim \n If you wouldnt show your friends/family it, dont post it (eg: dont post anything offensive)'.format(guild.name))

if __name__ == "__main__":
    # When running this file, if it is the 'main' file
    # I.E its not being imported from another python file run this
    for file in os.listdir(cwd + "/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f"cogs.{file[:-3]}")
            
menu = DefaultMenu('◀️', '▶️', '❌')
client.help_command = PrettyHelp(navigation=menu, color=Color.teal()) 

load_dotenv()
if os.getenv("SENTRY_URL"):
    import sentry_sdk
    sentry_sdk.init(os.getenv("SENTRY_URL"))
client.run(os.getenv("DISCORD_TOKEN"))