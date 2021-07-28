import random
import uuid
import asyncio
import discord
from discord import message
from discord.ext import commands
from pathlib import Path
from discord.ext.tasks import loop
import os, os.path
from logging import getLogger, DEBUG, INFO, WARNING, ERROR, CRITICAL
class Get(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.command(brief='Gets a random Meme', description='Gets a random Meme', aliases=["randomeme", "rdmmeme", "rdmeme"])
    async def randommeme(self, ctx):
            bot_message = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./meme/')
            file_name = random.choice(image)  # Selects a random element from the list
            path = "./meme/" + file_name
            await ctx.send(file_name, file=discord.File(path))
            await bot_message.delete()
            self.logger.log(INFO, f"{ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}) ran command randommeme, outputted %s", file_name)


    @commands.command(brief='Gets a random pet', description='Gets a random pet', aliases=["rdmpet", "rdpet"])
    async def randompet(self, ctx):
            bot_message = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./pet/')
            file_name = random.choice(image)  # Selects a random element from the list
            path = "./pet/" + file_name
            file = discord.File(path)
            await ctx.send(file_name, file=file)
            await bot_message.delete()
            self.logger.log(INFO, f"{ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}) ran command randompet, outputted %s", file_name)


    @commands.command(brief='Gets a certain meme', description='Gets a certain meme', aliases=["ctmeme", "ctm"])
    async def certainmeme(self, ctx, *, arg):
        p = (Path(os.curdir) / arg).resolve()
        if p.parent != Path(os.curdir).resolve():
            await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
            return
        else:
            bot_message = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./meme/')
            file_name = arg  
            path = "./meme/" + file_name
            file = discord.File(path)
            await ctx.send(file_name, file=file)
            await bot_message.delete()
        self.logger.log(INFO, f"{ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}) ran command certainmeme, sent %s", file_name)

    @commands.command(brief='Gets a certan pet', description='Gets a certan pet', aliases=["ctpet", "ctp"])
    async def certainpet(self, ctx, *, arg):
        p = (Path(os.curdir) / arg).resolve()
        if p.parent != Path(os.curdir).resolve():
            await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
            return
        else:
            bot_message = await ctx.send("<a:loading:851251570971770920> sending...")
            image = os.listdir('./pet/')
            file_name = arg  
            path = "./pet/" + file_name
            file = discord.File(path)
            await ctx.send(file_name, file=file)
            await bot_message.delete()
        self.logger.log(INFO, f"{ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}) ran command certainpet, sent %s", file_name)

    @commands.command(brief='Shows all of the memes', description='Shows all of the memes')
    async def allmemes(self, ctx):

        meme_list = discord.File('./meme.txt')
        await ctx.send(f'(updates every 2 minutes)', file=meme_list)
        self.logger.log(INFO, f"{ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}) ran command allmemes")
    @commands.command(brief='Shows all of the pets', description='Shows all of the pets')
    async def allpets(self, ctx):
        pet_list = discord.File('./pet.txt')
        await ctx.send(f'(updates every 2 minutes)', file=pet_list)
        self.logger.log(INFO, f"{ctx.author.name}#{ctx.author.discriminator} (ID: {ctx.author.id}) ran command allpets")


def setup(bot):
    bot.add_cog(Get(bot))