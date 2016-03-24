from unittest import TestCase
from util.commons_util.fundamentals.class_hierarchy import *
__author__ = 'Daniel'


class TestProperty(TestCase):
    def test_property_setter(self):
        r = VoltageResistance(ohms=10)
        r.voltage = 10
        self.assertEquals(r.current, 1)