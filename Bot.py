import os
from discord.ext.commands import Bot
from dotenv import load_dotenv

client = Bot(command_prefix = '#') 

load_dotenv()
client.run(os.getenv("DISCORD_TOKEN"))