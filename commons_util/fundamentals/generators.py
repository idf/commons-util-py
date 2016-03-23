"""
Prefer `yield` over returning a ret, where ret = []
"""
__author__ = 'Danyang'


def drange(start, stop, step):
    r = start
    while r<stop:
        yield r
        r += step

def frange(start, stop, step):
    return list(drange(start, stop, step))