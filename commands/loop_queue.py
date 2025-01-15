def loop_queue(bot, queue, played_songs, loop_flags):
    @bot.command()
    async def loop_queue(ctx):
        if not played_songs:
            await ctx.send('No songs have been played yet to loop.')
            return

        loop_flags["is_looping"] = True
        loop_flags["loop_type"] = "queue"
        queue.extend(played_songs)
        await ctx.send('Looping the entire queue infinitely.')
        
        if not ctx.voice_client.is_playing():
            await play_next(ctx, queue, played_songs, bot, loop_flags)
