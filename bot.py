import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from commands import register_commands
from events import register_events
from env import load_environment

load_environment()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
MEDIA_DIR = os.getenv('MEDIA_DIR')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
queue = []
played_songs = []

register_commands(bot, queue, played_songs, MEDIA_DIR)
register_events(bot)

bot.run(TOKEN)
