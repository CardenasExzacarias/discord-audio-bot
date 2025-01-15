def skip(bot):
    @bot.command()
    async def skip(ctx):
        voice_client = ctx.voice_client
        if voice_client.is_playing():
            voice_client.stop()
            await ctx.send('Skipped the current song.')
        else:
            await ctx.send('No song is currently playing.')