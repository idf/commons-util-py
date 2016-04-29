from unittest import TestCase
from util.commons_util.fundamentals.generators import *
__author__ = 'Daniel'


class TestGenerator(TestCase):
    def test_coroutine(self):
        itr = first_coroutine()
        itr.next()  # advance to first yield
        self.assertEquals(itr.send(1), "Received: 1")
        self.assertEquals(itr.send(2), "Received: 2")

    def test_yieldmin(self):
        itr = minimize()
        next(itr)
        self.assertEquals(itr.send(10), 10)
        self.assertEquals(itr.send(4), 4)
        self.assertEquals(itr.send(22), 4)
        self.assertEquals(itr.send(-1), -1)
