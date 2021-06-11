  
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

load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))