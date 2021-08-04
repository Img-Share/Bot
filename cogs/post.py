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
from aiohttp import ClientSession
import os.path
class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.command(brief='Posts A Meme to the Meme folder', description='Posts A Meme to the Meme folder')
    async def postmeme(self, ctx, *, arg):
        with sentry_sdk.start_span(op='postmeme', description="Posts a meme to the meme folder") as span:
            if len(arg.split(" ")) > 1:
                # it's a URL!
                async with ClientSession() as session:
                    async with session.get(arg.split(" ")[0]) as resp:
                        p = (Path(os.curdir) / arg).resolve()
                        with p.open('wb') as f:
                            if p.parent != Path(os.curdir).resolve():
                                await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
                                return 
                            async for data in resp.content.iter_chunked(1024):
                                f.write(data)
            else:
                p = (Path(os.curdir) / arg).resolve()
                if p.parent != Path(os.curdir).resolve():
                    await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
                    return
                else:
                    span.set_tag('file', arg)
                    _, ext = os.path.splittext(ctx.attachments[0].filename) 
                    imageName = './meme/' + arg + ext
                    await ctx.message.attachments[0].save(imageName)
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