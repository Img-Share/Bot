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
import os.path, os
from urllib.parse import urlparse
import re
class Post(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.logger = getLogger(__name__)

    @commands.command(brief='Posts A Meme to the Meme folder', description='Posts A Meme to the Meme folder')
    async def postmeme(self, ctx, *, arg=None):
        with sentry_sdk.start_span(op='postmeme', description="Posts a meme to the meme folder") as span:
            regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            if len(arg.split(" ")) > 1:
                # it's a URL!
                async with ClientSession() as session:
                    async with session.get(arg.split(" ")[0]) as resp:
                        _, ext = os.path.splittext(os.path.basename(urlparse(resp.url).path)) 
                        p = (Path(os.curdir) / (arg.split(" ")[1] + ext)).resolve()
                        with p.open('wb') as f:
                            if p.parent != Path(os.curdir).resolve():
                                await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
                                return 
                            async for data in resp.content.iter_chunked(1024):
                                f.write(data)
            elif re.match(regex, arg) and len(arg.split(" ")) == 1:
                # it's a URL!
                # but... no file name was provided
                async with ClientSession() as session:
                    async with session.get(arg) as resp:
                        arg = os.path.basename(urlparse(arg).path)
                        p = (Path(os.curdir) / arg).resolve()
                        if p.parent != Path(os.curdir).resolve():
                            await ctx.send(f'thats a bit sussy :flushed: (dont use ".." or "/" in your file name)')
                            return 
                        p = Path(os.path.join("meme", os.path.relpath(p)))
                        with open(p, 'wb') as f:
                            async for data in resp.content.iter_chunked(1024):
                                f.write(data)
            else:
                if not arg:
                    # no file name was provided
                    # get it from the attachment
                    arg = ctx.message.attachments[0].filename
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