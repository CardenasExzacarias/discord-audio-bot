from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')
MEDIA_DIR = os.getenv('MEDIA_DIR')