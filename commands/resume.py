def resume(bot):
    @bot.command()
    async def resume(ctx):
        voice_client = ctx.voice_client
        if voice_client.is_paused():
            voice_client.resume()
            await ctx.send('Resumed the audio.')
        else:
            await ctx.send('Audio is not paused.')
