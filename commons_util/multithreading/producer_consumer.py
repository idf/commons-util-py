"""
The problem with while True check & sleep:
  1. worker busy waits and constantly checks queue
  2. worker executes forever
  3. buffer grows
busy waiting, stopping workers, and memory explosion.

Solution: thread-safe queue
"""
from Queue import Queue
from threading import Thread
import time

__author__ = 'Daniel'


class SimpleProducerConsumer(object):
    """
    blocking get and put
    """
    def __init__(self):
        self.queue = Queue(1)

    def consumer(self):
        time.sleep(0.1)
        self.queue.get()  # block until .put(obj)
        print('Consumer got 1')
        self.queue.get()
        print('Consumer got 2')

    def run(self):
        thread = Thread(target=self.consumer)
        thread.start()

        self.queue.put(object())
        print('Producer put 1')
        self.queue.put(object())  # block until .get() since buffer size 1
        print('Producer put 2')
        thread.join()
        print('Producer done')

    def consumer_queue_join(self):
        time.sleep(0.1)
        self.queue.get()  # block until .put(obj)
        print('Consumer got 1')
        self.queue.get()
        print('Consumer got 2')
        self.queue.task_done()

    def run_queue_join(self):
        thread = Thread(target=self.consumer_queue_join())
        thread.start()

        self.queue.put(object())
        print('Producer put 1')
        self.queue.put(object())
        print('Producer put 2')
        self.queue.join()  # no need to join the thread pool
        print('Producer done')


class ClosableQueue(Queue):
    STOP = object()
    def close(self):
        self.put(self.STOP)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.STOP: return  # causes the thread to exit
                yield item
            finally:
                self.task_done()


class StoppableWorker(Thread):
    def __init__(self, func, in_queue, out_queue):
        self.func = func
        self.in_queue = in_queue
        self.out_queue = out_queue

    def run(self):
        for item in self.in_queue:
            result = self.func(item)
            self.out_queue.put(result)

    @staticmethod
    def test():
        download_queue = ClosableQueue()
        resize_queue = ClosableQueue()
        upload_queue = ClosableQueue()
        done_queue = ClosableQueue()
        threads = [
            StoppableWorker(lambda x: x, download_queue, resize_queue),
            StoppableWorker(lambda x: x, resize_queue, upload_queue),
            StoppableWorker(lambda x: x, upload_queue, download_queue)
        ]

        for thread in threads:
            thread.start()

        N = 1000
        for _ in xrange(N):
            download_queue.put(object())

        download_queue.close()
        download_queue.join()

        resize_queue.close()
        resize_queue.join()

        upload_queue.close()
        upload_queue.join()

        assert done_queue.qsize() == N