def _commands(bot):
    @bot.command(name='commands')
    async def _commands(ctx):
        help_text = """
        **Available Commands:**
        - **!join**: Make the bot join your voice channel.
        - **!play <filename or partial name>**: Play the specified audio or video file from your PC.
        - **!pause**: Pause the currently playing audio or video.
        - **!resume**: Resume the paused audio or video.
        - **!stop**: Stop the currently playing audio or video.
        - **!skip**: Skip to the next song or video in the queue.
        - **!replay**: Start/Stop replaying the actual audio or video.
        - **!leave**: Disconnect the bot from the voice channel.
        - **!loop**: Start/Stop looping the actual queue.
        - **!print**: Print the queue.
        - **!commands**: List all commands with a brief description.
        """
        await ctx.send(help_text)
