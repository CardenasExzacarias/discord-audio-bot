def pause(bot):
    @bot.command()
    async def pause(ctx):
        voice_client = ctx.voice_client
        if voice_client.is_playing():
            voice_client.pause()
            await ctx.send('Paused the audio.')
        else:
            await ctx.send('No audio is currently playing.')
