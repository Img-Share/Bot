import random
import uuid
import asyncio
import discord
from discord import message
from discord.ext import commands
from pathlib import Path
from discord.ext.tasks import loop
import os, os.path
class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(brief='Shows the Guidelines', description='Shows the Guidelines', aliases=["rule", "rules"])
    async def guidelines(self, ctx):
        await ctx.send(f'Guidelines: \n No NSFW \n No Deepfakes (looking at you <@729135459405529118> <:eyes_sus:851168417453047808>) \n No Racisim \n If you wouldnt show your friends/family it, dont post it (eg: dont post anything offensive)')

    @commands.command(brief='Sends an invite to join the official Img.Share server', description='Sends an invite to join the official Img.Share server')
    async def server(self, ctx):
        await ctx.send(f'https://discord.gg/MrtBFFQk3k')
        print(f'someone just sent and invite to join the server!')

    @commands.command(brief='Sends an invite to the bot', description='Sends an invite to the bot')
    async def invite(self, ctx):
        await ctx.send(f'https://www.thediamondk.com/bot.html')
        print(f'someone just invited the bot!')

    @commands.command(brief='Pings the bot', description='Pings the bot')
    async def ping(self, ctx):
        await ctx.send(f'`{round(self.bot.latency * 1000)} ms`')
        print(f'the bot was pinged' f' ({round(self.bot.latency * 1000)} ms)')


def setup(bot):
    bot.add_cog(Other(bot))