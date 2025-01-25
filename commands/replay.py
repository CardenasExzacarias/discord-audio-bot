import os

def replay(bot, player_queue):
    @bot.command()
    async def replay(ctx):
        player_queue.replay()
        if player_queue.is_replaying:
            await ctx.send(f'Start replaying: "{os.path.basename(player_queue.head.path)}"')
        else:
            await ctx.send(f'Stop replaying: "{os.path.basename(player_queue.head.path)}"')