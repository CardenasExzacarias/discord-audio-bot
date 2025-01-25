def print(bot, player_queue):
    @bot.command()
    async def print(ctx):
        await ctx.send(f'"{player_queue}"')