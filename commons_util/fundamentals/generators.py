"""
Prefer `yield` over returning a ret, where ret = []

# Communication
Think of it like this, with a generator and no send, it's a one way street

==========       yield      ========
Generator |   ------------> | User |
==========                  ========
But with send, it becomes a two way street

==========       yield       ========
Generator |   ------------>  | User |
==========    <------------  ========
                  send


# Yield & Send
bar = yield foo
  After yield foo, wait for send(val) to assign val to bar
  The value of the yield expression will be the value was passed to the
  generator's send method from the exterior code.
"""
__author__ = 'Danyang'


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step


def frange(start, stop, step):
    return list(drange(start, stop, step))


def first_coroutine():
    received = yield
    while True:
        received = yield "Received: %s" % str(received)


def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)
