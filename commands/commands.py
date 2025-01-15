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
        - **!replay**: Replay the last song or video played.
        - **!leave**: Disconnect the bot from the voice channel.
        - **!loop**: Loop the last played song or video.
        - **!loop_queue**: Loop the entire queue of played songs or videos.
        - **!stop_loop**: Stop looping.
        - **!commands**: List all commands with a brief description.
        """
        await ctx.send(help_text)
