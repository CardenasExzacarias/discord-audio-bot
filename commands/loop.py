def loop(bot, player_queue):
    @bot.command()
    async def loop(ctx):
        player_queue.loop()
        if player_queue.is_looping:
            await ctx.send('Start looping the queue')
        else:
            await ctx.send('Stop looping the queue')