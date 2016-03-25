"""
Multi-threading with GIL in python is useful for blocking I/O

# Threads to make multiple system calls in parallel
Threading with the system calls will all run in parallel from multiple Python
threads even though they're limited by the GIL. The GIL prevents my Python code
from running in parallel, but it has no negative effect on system calls.
This works because Python threads release the GIL just before they make system
calls and reacquire the GIL as soon as the system calls are done.
"""

import threading
from util.commons_util.decorators.classes import *
__author__ = 'Danyang'


def print_msg(name, msg):
    print "%s says: %s" % (name, msg)


class AbstractThread(threading.Thread):
    """
    e.g.
      thread = Thread(target=some_func)
      thread.start()
      threat.join()
    """
    @Override(threading.Thread)
    def __init__(self, name, production=False):
        super(AbstractThread, self).__init__()
        self.name = name
        self.production = production

    def print_msg(self, msg):
        print_msg(self.name, msg)