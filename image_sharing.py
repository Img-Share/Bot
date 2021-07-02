import random
import uuid
import asyncio
import discord
from discord import message
from discord.ext import commands
from pathlib import Path
from discord.ext.tasks import loop
from discord_slash.cog_ext import cog_slash
import os
class ImageSharing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @cog_slash(description='Shows the Guidelines', aliases=["rule", "rules"])
    async def guidelines(self, ctx):
        await ctx.send(f'Guidelines: \n No NSFW \n No Deepfakes (looking at you <@729135459405529118> <:eyes_sus:851168417453047808>) \n No Racisim \n If you wouldnt show your friends/family it, dont post it (eg: dont post anything offensive)')

    @cog_slash(description='Sends an invite to join the official Img.Share server')
    async def server(self, ctx):
        await ctx.send(f'https://discord.gg/MrtBFFQk3k')
        print(f'someone just sent and invite to join the server!')

    @cog_slash(description='Sends an invite to the bot')
    async def invite(self, ctx):
        await ctx.send(f'https://www.thediamondk.com/bot.html')
        print(f'someone just invited the bot!')

    @cog_slash(description='Pings the bot')
    async def ping(self, ctx):
        await ctx.send(f'`{round(self.bot.latency * 1000)} ms`')
        print(f'the bot was pinged' f' ({round(self.bot.latency * 1000)} ms)')

    @cog_slash(description='Gets a random Meme', aliases=["randomeme", "rdmmeme", "rdmeme"])
    async def randommeme(self, ctx, *, args):
            BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./meme/')
            imgString = random.choice(image)  # Selects a random element from the list
            path = "./meme/" + imgString
            await ctx.send((imgString), file=discord.File(path))
            await BotMessage.delete()

    @cog_slash(description='Posts A Meme to the Meme folder')
    async def postmeme(self, ctx, *, arg):
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

    @cog_slash(description='Posts A Meme Video to the Meme folder')
    async def postmemevideo(self, ctx, *, arg):
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

    @cog_slash(description='Gets a random pet', aliases=["rdmpet", "rdpet"])
    async def randompet(self, ctx, *, args):
            BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./pet/')
            imgString = random.choice(image)  # Selects a random element from the list
            path = "./pet/" + imgString
            await ctx.send((imgString), file=discord.File(path))
            await BotMessage.delete()

    @cog_slash(description='Posts A pet to the pet folder')
    async def postpet(self, ctx, *, arg):
        p = (Path(os.curdir) / arg).resolve()
        if p.parent != Path(os.curdir).resolve():
            await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
            return
        else:
            imageName = './pet/' + arg + '.png'
            await ctx.message.attachments[0].save(imageName)
            await ctx.send(f'Posted <:ImgShareCheck:851852314217283645>')
            print(imageName) 
            print('was added to the pet folder')

    @cog_slash(description='Gets a certain meme', aliases=["ctmeme", "ctm"])
    async def certainmeme(self, ctx, *, arg):
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

    @cog_slash(description='Gets a certan pet', aliases=["ctpet", "ctp"])
    async def certainpet(self, ctx, *, arg):
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

    @cog_slash(description='Shows all of the memes')
    async def allmemes(self, ctx):
        await ctx.send((f'(updates every 2 minutes)'), file=discord.File('/home/pi/Desktop/Bots/Discord/Img.Share/Bot/meme.txt'))

    @cog_slash(description='Shows all of the pets')
    async def allpets(self, ctx):
        await ctx.send((f'(updates every 2 minutes)'), file=discord.File('/home/pi/Desktop/Bots/Discord/Img.Share/Bot/pet.txt'))

    @cog_slash(description='admin command')
    async def breaktest(self, ctx, *, arg):
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

def setup(bot):
    bot.add_cog(ImageSharing(bot))