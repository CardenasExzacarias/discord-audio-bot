import os
from .play_audio import play_audio
from .play_video import play_video

def player(bot, queue, played_songs, media_dir, loop_flags):
    @bot.command()
    async def play(ctx, *, query):
        voice_client = ctx.voice_client
        if not voice_client or not voice_client.is_connected():
            await ctx.send('Bot is not connected to a voice channel.')
            return

        matches = [f for f in os.listdir(media_dir) if query.lower() in f.lower()]
        if not matches:
            await ctx.send(f'No files matching "{query}" found.')
            return

        file_path = os.path.join(media_dir, matches[0])
        queue.append(file_path)

        if not voice_client.is_playing():
            if file_path.endswith(('.mp3', '.wav')):
                await play_audio(ctx, queue, played_songs, bot, loop_flags, file_path)
            elif file_path.endswith(('.mp4', '.mkv', '.avi')):
                await play_video(ctx, queue, played_songs, bot, loop_flags, file_path)
