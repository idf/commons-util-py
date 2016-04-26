"""
# Timeout a long running function with the default expiry of 10 seconds.
@timeout
def long_running_function1():
    ...

# Timeout after 5 seconds
@timeout(5)
def long_running_function2():
    ...

# Timeout after 30 seconds, with the error "Connection timed out"
@timeout(30, os.strerror(errno.ETIMEDOUT))
def long_running_function3():
    ...

Beware that this is not thread-safe: if you're using multithreading, the signal
will get caught by a random thread. For single-threaded programs though, this
is the easiest solution.

Reference: http://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish
"""
from functools import wraps
import errno
import os
import signal
__author__ = 'Daniel'


class TimeoutError(Exception):
    pass


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator
