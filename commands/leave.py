def leave(bot):
    @bot.command()
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.guild.voice_client.disconnect()
            await ctx.send('Disconnected from the voice channel.')
        else:
            await ctx.send('The bot is not connected to a voice channel.')