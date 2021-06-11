import os
from discord.ext.commands import Bot
from discord.ext import find
from dotenv import load_dotenv

client = Bot(command_prefix = '#') 
@client.event
async def on_command_error(ctx, error):
    await ctx.send(f"Error! <:ImgShareError:851852314242973746> did you fill out everything correctly? (Error Message: {str(error)})")
    print(str(error))
    
    
@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Guidelines: \n No NSFW \n No Deepfakes (looking at you <@729135459405529118> <:eyes_sus:851168417453047808>) \n No Racisim \n If you wouldnt show your friends/family it, dont post it (eg: dont post anything offensive)'.format(guild.name))
    
load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))