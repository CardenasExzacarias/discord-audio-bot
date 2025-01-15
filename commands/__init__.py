from .join import join
from .play import play
from .pause import pause
from .resume import resume
from .stop import stop
from .skip import skip
from .leave import leave
from .replay import replay
from .commands import _commands
from .loop import loop
from .loop_queue import loop_queue
from .stop_loop import stop_loop

def register_commands(bot, queue, played_songs, media_dir):
    loop_flags = {"is_looping": False, "loop_type": None, "stopped": False}

    join(bot)
    play(bot, queue, played_songs, media_dir, loop_flags)
    pause(bot)
    resume(bot)
    stop(bot, loop_flags)
    skip(bot)
    leave(bot)
    replay(bot, queue, played_songs)
    _commands(bot)
    loop(bot, queue, played_songs, loop_flags)
    loop_queue(bot, queue, played_songs, loop_flags)
    stop_loop(bot, queue, loop_flags)
