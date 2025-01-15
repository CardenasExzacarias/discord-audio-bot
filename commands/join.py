def join(bot):
    @bot.command()
    async def join(ctx):
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f'Joined {channel}')
        else:
            await ctx.send('You are not connected to a voice channel.')
