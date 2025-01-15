def stop(bot, loop_flags):
    @bot.command()
    async def stop(ctx):
        loop_flags["stopped"] = True
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        await ctx.send('Playback stopped.')
