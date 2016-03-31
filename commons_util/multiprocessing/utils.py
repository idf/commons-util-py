__author__ = 'Danyang'
from multiprocessing import Value, Lock


class Counter(object):
    def __init__(self):
        self.val = Value('i', 0)

    def increment(self, n=1):
        with self.val.get_lock():
            self.val.value += n

    @property
    def value(self):
        with self.val.get_lock():
            return self.val.value


class LockingCounter(object):
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset
