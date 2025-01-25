import os
from .play_audio import play_audio
from .play_video import play_video

def player(bot, player_queue, media_dir):
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
        player_queue.enqueue(file_path)
        await ctx.send(f'"{os.path.basename(player_queue.tail.path)}" Has been enqueued.')

        if not voice_client.is_playing():
            if file_path.endswith(('.mp3', '.wav')):
                await play_audio(ctx, player_queue, bot)
            elif file_path.endswith(('.mp4', '.mkv', '.avi')):
                await play_video(ctx, player_queue, bot)
