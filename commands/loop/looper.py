def looper(bot, queue, played_songs, loop_flags):
    @bot.command()
    async def loop(ctx):
        if not played_songs:
            await ctx.send('No songs have been played yet to loop.')
            return

        loop_flags["is_looping"] = True
        loop_flags["loop_type"] = "song"
        file_path = played_songs[-1]
        queue.insert(0, file_path)
        await ctx.send('Looping the last song infinitely.')
        
        if not ctx.voice_client.is_playing():
            await play_next(ctx, queue, played_songs, bot, loop_flags)
