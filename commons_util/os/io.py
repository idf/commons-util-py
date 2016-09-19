import sys


__author__ = 'Daniel'


class IOStreamer(object):
    @staticmethod
    def stdinlines():
        for line in sys.stdin.readlines():
            yield line.strip()
