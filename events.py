from discord.ext import commands

def register_events(bot):

    @bot.event
    async def on_ready():
        print(f'Bot connected as {bot.user}')
        for guild in bot.guilds:
            print(f'Connected to guild: {guild.name} (ID: {guild.id})')

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("I don't know that command. You can type `!commands` to list all the commands.")
        else:
            raise error
