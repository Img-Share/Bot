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


    @commands.command(breif="Reload all/one of the bots cogs!")
    @commands.is_owner()
    async def reload(self, ctx, cog=None):
        if not cog:
            # No cog, means we reload all cogs
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x0e6668,
                    timestamp=ctx.message.created_at
                )
                for ext in os.listdir("./cogs/"):
                    if ext.endswith(".py") and not ext.startswith("_"):
                        try:
                            self.bot.unload_extension(f"cogs.{ext[:-3]}")
                            self.bot.load_extension(f"cogs.{ext[:-3]}")
                            embed.add_field(
                                name=f"Reloaded: `{ext}`",
                                value='\uFEFF',
                                inline=False
                            )
                        except Exception as e:
                            embed.add_field(
                                name=f"Failed to reload: `{ext}`",
                                value=e,
                                inline=False
                            )
                        await asyncio.sleep(0.5)
                await ctx.send(embed=embed)
        else:
            # reload the specific cog
            async with ctx.typing():
                embed = discord.Embed(
                    title="Reloading all cogs!",
                    color=0x0e6668,
                    timestamp=ctx.message.created_at
                )
                ext = f"{cog.lower()}.py"
                if not os.path.exists(f"./cogs/{ext}"):
                    # if the file does not exist
                    embed.add_field(
                        name=f"Failed to reload: `{ext}`",
                        value="This cog does not exist.",
                        inline=False
                    )

                elif ext.endswith(".py") and not ext.startswith("_"):
                    try:
                        self.bot.unload_extension(f"cogs.{ext[:-3]}")
                        self.bot.load_extension(f"cogs.{ext[:-3]}")
                        embed.add_field(
                            name=f"Reloaded: `{ext}`",
                            value='\uFEFF',
                            inline=False
                        )
                    except Exception:
                        desired_trace = traceback.format_exc()
                        embed.add_field(
                            name=f"Failed to reload: `{ext}`",
                            value=desired_trace,
                            inline=False
                        )
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Other(bot))