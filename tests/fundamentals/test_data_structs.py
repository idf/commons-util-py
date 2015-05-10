import random
from unittest import TestCase
from commons_util.fundamentals.data_structs import *
__author__ = 'Danyang'


class TestDataStructs(TestCase):
    def test_argsort(self):
        A = [3, 2, 1]
        ret = Sorter.argsort(A)
        self.assertEqual(ret, [2, 1, 0])

    def test_excel_column(self):
        col = ExcelColumn()
        self.assertEqual(list(col.columns(800))[-1], 'adt')


class TestDisplayer(TestCase):
    def test_display(self):
        dis = Displayer()
        class A(object):
            def __init__(self):
                self.a = "abc"
                self.b = 1.0

        class B(object):
            def __init__(self):
                self.a = A()
                self.b = 1.0
        b = B()

        self.assertEqual(str(dis.dump(b)), '{"a": {"a": "abc", "b": 1.0}, "b": 1.0}')
        b_str = """{
    "a": {
        "a": "abc",
        "b": 1.0
    },
    "b": 1.0
}"""
        self.assertEqual(dis.display(b), b_str)


class TestSearcher(TestCase):
    def test_binary_search(self):
        rand_lst = [int(1000*random.random()) for _ in xrange(100)]
        target = rand_lst[0]
        rand_lst.sort()

        def predicate(idx):
            if rand_lst[idx]==target:
                return 0
            elif rand_lst[idx]<target:
                return -1
            else:
                return 1

        idx = Searcher.binary_search(0, 100, predicate)
        self.assertEqual(target, rand_lst[idx])


class TestWrapper(TestCase):
    def test_unpack(self):
        x = [random.randint(0, 100) for _ in xrange(100)]  # () for generators
        y = [random.randint(0, 100) for _ in xrange(100)]
        lst = zip(x, y)
        a, b = Wrapper.unpack(lst)  # generator
        self.assertEqual(a, tuple(x))
        self.assertEqual(b, tuple(y))

