import random
import uuid
import asyncio
import discord
from discord import message
from discord.ext import commands
from pathlib import Path
from discord.ext.tasks import loop
import os, os.path
from logging import getLogger, ERROR, CRITICAL, INFO, WARNING, DEBUG
import sentry_sdk
class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.command(brief='Posts A Meme to the Meme folder', description='Posts A Meme to the Meme folder')
    async def postmeme(self, ctx, *, arg):
        with sentry_sdk.start_span(op='postmeme', description="Posts a meme to the meme folder") as span:
            p = (Path(os.curdir) / arg).resolve()
            if p.parent != Path(os.curdir).resolve():
                await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
                return
            else:
                span.set_tag('file', arg)
                imageName = './meme/' + arg + '.png'
                await ctx.message.attachments[0].save(imageName)
                await ctx.send(f'Posted <:ImgShareCheck:851852314217283645>')
                self.logger.log(INFO, f"{arg} was just added to the meme folder")

    @commands.command(brief='Posts A Meme Video to the Meme folder', description='Posts A Meme Video to the Meme folder')
    async def postmemevideo(self, ctx, *, arg):
        with sentry_sdk.start_span(op='postmeme', description="Posts a meme to the meme folder") as span:
            p = (Path(os.curdir) / arg).resolve()
            if p.parent != Path(os.curdir).resolve():
                await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
                return
            else:
                span.set_tag('file', arg)
                VideoName = './meme/' + arg + '.mp4'
                await ctx.message.attachments[0].save(VideoName)
                await ctx.send(f'Posted <:ImgShareCheck:851852314217283645>')
                self.logger.log(INFO, f"{arg} was just added to the meme folder")

    @commands.command(brief='Posts A pet to the pet folder', description='Posts A pet to the pet folder')
    async def postpet(self, ctx, *, arg):
        with sentry_sdk.start_span(op='postpet', description="Posts a pet to the meme folder") as span:
            p = (Path(os.curdir) / arg).resolve()
            if p.parent != Path(os.curdir).resolve():
                await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
                return
            else:
                span.set_tag('file', arg)
                imageName = './pet/' + arg + '.png'
                await ctx.message.attachments[0].save(imageName)
                self.logger.log(INFO, f"{arg} was just added to the pet folder")

def setup(bot):
    bot.add_cog(Post(bot))