import heapq

__author__ = 'Daniel'


class Heap(object):
    def __init__(self, data=None, key=lambda x: None):
        self.heap = data or None
        heapq.heapify(self.heap)
        self.key = key

    def push(self, item):
        if self.key:
            item = (self.key(item), item)

        heapq.heappush(self.heap, item)

    def pop(self):
        item = heapq.heappop(self.heap)
        return item[1] if self.key else item