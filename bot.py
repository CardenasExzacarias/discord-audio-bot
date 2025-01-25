import discord
from discord.ext import commands
from commands import register_commands
from events import register_events
from env import TOKEN, MEDIA_DIR
from player_queue.PlayerQueue import PlayerQueue

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

player_queue = PlayerQueue()

register_commands(bot, player_queue, MEDIA_DIR)
register_events(bot)

bot.run(TOKEN)