def stop(bot):
    @bot.command()
    async def stop(ctx):
        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()
        await ctx.send('Playback stopped.')
