def replay(bot, queue, played_songs):
    @bot.command()
    async def replay(ctx):
        if played_songs:
            file_path = played_songs[-1]
            queue.insert(0, file_path)
            await ctx.send('Replaying the last song.')
            if not ctx.voice_client.is_playing():
                await play_next(ctx, queue, played_songs)
        else:
            await ctx.send('No songs have been played yet.')