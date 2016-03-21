from unittest import TestCase
from util.commons_util.fundamentals.serialization import *
__author__ = 'Daniel'


class TestSerialization(TestCase):
    def test_todict(self):
        class BinaryTree(ToDictMixin):
            def __init__(self, value, left=None, right=None):
                self.value = value
                self.left = left
                self.right = right


        tree = BinaryTree(10,
                          left=BinaryTree(7, right=BinaryTree(9)),
                          right=BinaryTree(13, left=BinaryTree(11)))

        self.assertEquals(tree.to_dict(), {'right': {'right': None, 'value': 13, 'left': {'right': None, 'value': 11, 'left': None}}, 'value': 10, 'left': {'right': {'right': None, 'value': 9, 'left': None}, 'value': 7, 'left': None}})