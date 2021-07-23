import random
import uuid
import asyncio
import discord
from discord import message
from discord.ext import commands
from pathlib import Path
from discord.ext.tasks import loop
import os, os.path
class Get(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Gets a random Meme', description='Gets a random Meme', aliases=["randomeme", "rdmmeme", "rdmeme"])
    async def randommeme(self, ctx):
            BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./meme/')
            imgString = random.choice(image)  # Selects a random element from the list
            path = "./meme/" + imgString
            await ctx.send((imgString), file=discord.File(path))
            await BotMessage.delete()


    @commands.command(brief='Gets a random pet', description='Gets a random pet', aliases=["rdmpet", "rdpet"])
    async def randompet(self, ctx):
            BotMessage = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./pet/')
            imgString = random.choice(image)  # Selects a random element from the list
            path = "./pet/" + imgString
            await ctx.send((imgString), file=discord.File(path))
            await BotMessage.delete()


    @commands.command(brief='Gets a certain meme', description='Gets a certain meme', aliases=["ctmeme", "ctm"])
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

    @commands.command(brief='Gets a certan pet', description='Gets a certan pet', aliases=["ctpet", "ctp"])
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

    @commands.command(brief='Shows all of the memes', description='Shows all of the memes')
    async def allmemes(self, ctx):
        meme_list = discord.File('/home/pi/Desktop/Bots/Discord/Img.Share/Bot/meme.txt')
        await ctx.send(f'(updates every 2 minutes)', file=meme_list)

    @commands.command(brief='Shows all of the pets', description='Shows all of the pets')
    async def allpets(self, ctx):
        pet_list = discord.File('/home/pi/Desktop/Bots/Discord/Img.Share/Bot/pet.txt')
        await ctx.send(f'(updates every 2 minutes)', file=pet_list)


def setup(bot):
    bot.add_cog(Get(bot))