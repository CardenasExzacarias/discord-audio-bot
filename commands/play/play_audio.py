import os
import asyncio
import discord

async def play_audio(ctx, queue, played_songs, bot, loop_flags, file_path):
    voice_client = ctx.voice_client
    played_songs.append(file_path)

    ffmpeg_options = {
        'options': '-vn',
    }

    def after_playing(error):
        if not loop_flags["stopped"]:
            asyncio.run_coroutine_threadsafe(next_audio(ctx, queue, played_songs, bot, loop_flags), bot.loop).result()

    voice_client.play(discord.FFmpegPCMAudio(file_path, **ffmpeg_options), after=after_playing)
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source)
    voice_client.source.volume = 0.5

    await ctx.send(f'Now playing: {os.path.basename(file_path)}')

async def next_audio(ctx, queue, played_songs, bot, loop_flags):
    if queue and not loop_flags["stopped"]:
        if loop_flags.get("skipped"):
            loop_flags["skipped"] = False
            if queue:
                skipped_song = queue.pop(0)
                if loop_flags["is_looping"] and loop_flags["loop_type"] == "queue":
                    played_songs.append(skipped_song)

        if loop_flags["is_looping"] and not loop_flags["stopped"]:
            if loop_flags["loop_type"] == "queue" and played_songs:
                queue.extend(song for song in played_songs if song not in queue)

        if queue and not loop_flags["stopped"]:
            await play_audio(ctx, queue, played_songs, bot, loop_flags, queue.pop(0))
