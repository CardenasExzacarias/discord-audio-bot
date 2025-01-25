import os
import asyncio
import discord

async def play_audio(ctx, player_queue, bot):
    voice_client = ctx.voice_client

    ffmpeg_options = {
        'options': '-vn',
    }

    def after_playing(error):
        if not player_queue.is_empty():
            asyncio.run_coroutine_threadsafe(next_audio(ctx, player_queue, bot), bot.loop).result()

    if not player_queue.is_empty():
        voice_client.play(discord.FFmpegPCMAudio(player_queue.head.path, **ffmpeg_options), after=after_playing)
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
        voice_client.source.volume = 0.5
        message = f'Now playing: {os.path.basename(player_queue.head.path)}'
    else:
        message = "Queue is empty"
    await ctx.send(message)

async def next_audio(ctx, player_queue, bot):
    player_queue.dequeue()
    await play_audio(ctx, player_queue, bot)
