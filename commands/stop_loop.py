def stop_loop(bot, queue, loop_flags):
    @bot.command()
    async def stop_loop(ctx):
        loop_flags["is_looping"] = False
        loop_flags["loop_type"] = None
        queue.clear()
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        await ctx.send('Looping stopped and queue cleared.')
