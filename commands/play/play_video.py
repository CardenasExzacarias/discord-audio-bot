import os
import asyncio
import discord

async def play_video(ctx, queue, played_songs, bot, loop_flags, file_path):
    voice_client = ctx.voice_client
    played_songs.append(file_path)

    ffmpeg_options = {
        'options': '-vf "scale=1280:720"',
    }

    def after_playing(error):
        if not loop_flags["stopped"]:
            asyncio.run_coroutine_threadsafe(next_video(ctx, queue, played_songs, bot, loop_flags), bot.loop).result()

    voice_client.play(discord.FFmpegPCMAudio(file_path, **ffmpeg_options), after=after_playing)
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    voice_client.source.volume = 0.5

    await ctx.send(f'Now playing: {os.path.basename(file_path)}')

async def next_video(ctx, queue, played_songs, bot, loop_flags):
    if loop_flags["is_looping"] and not loop_flags["stopped"]:
        if loop_flags["loop_type"] == "song" and played_songs:
            file_path = played_songs[-1]
            queue.insert(0, file_path)
        elif loop_flags["loop_type"] == "queue":
            queue.extend(played_songs)
    if queue and not loop_flags["stopped"]:
        await play_video(ctx, queue, played_songs, bot, loop_flags, queue.pop(0))
