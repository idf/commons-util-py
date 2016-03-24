from unittest import TestCase
from util.commons_util.fundamentals.class_hierarchy import *
__author__ = 'Daniel'


class TestProperty(TestCase):
    def test_property_setter(self):
        r = VoltageResistance(ohms=10)
        r.voltage = 10
        self.assertEquals(r.current, 1)


class TestDescriptor(TestCase):
    def test_grade_descriptor(self):
        class Exam(object):
            math_grade = GradeDescriptor()
            writing_grade = GradeDescriptor()
            science_grade = GradeDescriptor()


        exam1 = Exam()
        exam2 = Exam()
        with self.assertRaises(ValueError):
            exam1.science_grade = 101

        exam1.science_grade = 99
        exam2.science_grade = 100
        self.assertEquals(exam1.science_grade, 99)
        self.assertEquals(exam2.science_grade, 100)
