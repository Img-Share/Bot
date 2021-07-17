import random
import uuid
import asyncio
import discord
from discord import message
from discord.ext import commands
from pathlib import Path
from discord.ext.tasks import loop
import os, os.path
class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='Posts A Meme to the Meme folder', description='Posts A Meme to the Meme folder')
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

    @commands.command(brief='Posts A Meme Video to the Meme folder', description='Posts A Meme Video to the Meme folder')
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

    @commands.command(brief='Posts A pet to the pet folder', description='Posts A pet to the pet folder')
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

def setup(bot):
    bot.add_cog(Post(bot))