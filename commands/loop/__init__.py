from .looper import looper
from .stop_loop import stop_loop
from .loop_queue import loop_queue

def loop(bot, queue, played_songs, loop_flags):
    looper(bot, queue, played_songs, loop_flags)
    stop_loop(bot, queue, loop_flags)
    loop_queue(bot, queue, played_songs, loop_flags)