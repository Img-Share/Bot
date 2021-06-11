  
import discord
import os
import random
import uuid
import asyncio
from discord import message
from discord.ext import commands
from discord.ext.commands import Bot
from dotenv import load_dotenv
from discord.utils import find
from pathlib import Path
from discord.ext.tasks import loop


client = commands.Bot(command_prefix = '#') 

@client.event
async def on_ready():
    print('holy crap it worked')
    client.loop.create_task(status_task())
    
    
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
async def on_command_error(ctx, error):
    await ctx.send(f"Error! <:ImgShareError:851852314242973746> did you fill out everything correctly? (Error Message: {str(error)})")
    print(str(error))
    
    
@client.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        await general.send('Guidelines: \n No NSFW \n No Deepfakes (looking at you <@729135459405529118> <:eyes_sus:851168417453047808>) \n No Racisim \n If you wouldnt show your friends/family it, dont post it (eg: dont post anything offensive)'.format(guild.name))
    

# Commands

@client.command(brief='Shows the Guidelines', description='Shows the Guidelines', aliases=["rule", "rules"])
async def guidelines(ctx):
    await ctx.send(f'Guidelines: \n No NSFW \n No Deepfakes (looking at you <@729135459405529118> <:eyes_sus:851168417453047808>) \n No Racisim \n If you wouldnt show your friends/family it, dont post it (eg: dont post anything offensive)')

@client.command(brief='Sends an invite to join the official Img.Share server', description='Sends an invite to join the official Img.Share server')
async def server(ctx):
    await ctx.send(f'https://discord.gg/MrtBFFQk3k')
    print(f'someone just sent and invite to join the server!')

@client.command(brief='Sends an invite to the bot', description='Sends an invite to the bot')
async def invite(ctx):
    await ctx.send(f'https://www.thediamondk.com/bot.html')
    print(f'someone just invited the bot!')

@client.command(brief='Pings the bot', description='Pings the bot')
async def ping(ctx):
    await ctx.send(f'`{round(client.latency * 1000)} ms`')
    print(f'the bot was pinged' f' ({round(client.latency * 1000)} ms)')

@client.command(brief='Gets a random Meme', description='Gets a random Meme', aliases=["randomeme", "rdmmeme", "rdmeme"])
async def randommeme(ctx, *args):
        BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
        image = os.listdir('./meme/')
        imgString = random.choice(image)  # Selects a random element from the list
        path = "./meme/" + imgString
        await ctx.send((imgString), file=discord.File(path))
        await BotMessage.delete()
        
@client.command(brief='Posts A Meme to the Meme folder', description='Posts A Meme to the Meme folder')
async def postmeme(ctx, *, arg):
    p = (Path(os.curdir) / arg).resolve()
    if p.parent != Path(os.curdir).resolve():
        await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
        return
    else:
        imageName = './meme/' + arg + '.png'
        await ctx.message.attachments[0].save(imageName)
        await ctx.send(f'Posted <:ImgShareCheck:851852314217283645>')
        print(imageName) 
        print('was added to the meme folder')

@client.command(brief='Posts A Meme Video to the Meme folder', description='Posts A Meme Video to the Meme folder')
async def postmemevideo(ctx, *, arg):
    p = (Path(os.curdir) / arg).resolve()
    if p.parent != Path(os.curdir).resolve():
        await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
        return
    else:
        VideoName = './meme/' + arg + '.mp4'
        await ctx.message.attachments[0].save(VideoName)
        await ctx.send(f'Posted <:ImgShareCheck:851852314217283645>')
        print(VideoName) 
        print('was added to the meme folder')

@client.command(brief='Gets a random pet', description='Gets a random pet', aliases=["rdmpet", "rdpet"])
async def randompet(ctx, *args):
        BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
        image = os.listdir('./pet/')
        imgString = random.choice(image)  # Selects a random element from the list
        path = "./pet/" + imgString
        await ctx.send((imgString), file=discord.File(path))
        await BotMessage.delete()

@client.command(brief='Posts A pet to the pet folder', description='Posts A pet to the pet folder')
async def postpet(ctx, *, arg):
    p = (Path(os.curdir) / arg).resolve()
    if p.parent != Path(os.curdir).resolve():
        await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
        return
    else:
        imageName = './pet/' + arg + '.png'
        await ctx.message.attachments[0].save(imageName)
        await ctx.send(f'Posted <:ImgShareCheck:851852314217283645>')
        print(imageName) 
        print('was added to the pet folder by')
    
@client.command(brief='Gets a certain meme', description='Gets a certain meme', aliases=["ctmeme", "ctm"])
async def certainmeme(ctx, *, arg):
    p = (Path(os.curdir) / arg).resolve()
    if p.parent != Path(os.curdir).resolve():
        await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
        return
    else:
        BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
        image = os.listdir('./meme/')
        imgString = arg  
        path = "./meme/" + imgString
        await ctx.send((imgString), file=discord.File(path))
        await BotMessage.delete()
        
@client.command(brief='Gets a certan pet', description='Gets a certan pet', aliases=["ctpet", "ctp"])
async def certainpet(ctx, *, arg):
    p = (Path(os.curdir) / arg).resolve()
    if p.parent != Path(os.curdir).resolve():
        await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
        return
    else:
        BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
        image = os.listdir('./pet/')
        imgString = arg  
        path = "./pet/" + imgString
        await ctx.send((imgString), file=discord.File(path))
        await BotMessage.delete()
        
@client.command(brief='Shows all of the memes', description='Shows all of the memes')
async def allmemes(ctx):
    await ctx.send((f'(updates every 2 minutes)'), file=discord.File(os.curdir + '/meme.txt'))
    
@client.command(brief='Shows all of the pets', description='Shows all of the pets')
async def allpets(ctx):
    await ctx.send((f'(updates every 2 minutes)'), file=discord.File(os.curdir + '/pet.txt'))
    
@client.command(brief='admin command', description='admin command')
async def breaktest(ctx, *, arg):
    p = (Path(os.curdir) / arg).resolve()
    if p.parent != Path(os.curdir).resolve():
        await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
        return
    else:
        imageName = './breaktest/' + arg + '.png'
        await ctx.message.attachments[0].save(imageName)
        await ctx.send(f'Invalid Permissions')
        print(imageName) 
        print('was added to the breaktest folder')
    
@client.command(bref="Posts a random Nintendo music video")
async def randommusic(ctx):
    music = [
        "https://www.youtube.com/watch?v=zW0Gn2ZV6Ys",
        "https://www.youtube.com/watch?v=Zy6hbtm3hrI",
        "https://www.youtube.com/watch?v=Ya8Sng3mZqA"
    ]
    await ctx.send(random.choice(music))
load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))