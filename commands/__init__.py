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
from .print import print

def register_commands(bot, player_queue, media_dir):
    join(bot)
    play(bot, player_queue, media_dir)
    pause(bot)
    resume(bot)
    replay(bot, player_queue)
    loop(bot, player_queue)
    skip(bot)
    stop(bot)
    leave(bot)
    print(bot, player_queue)
    _commands(bot)
