"""
When you're building a complex class hierarchy, you may want to enforce style,
require overriding methods, or have strict relationships between class
attributes. Metaclasses enable these use cases by providing a reliable way to
run your validation code each time a new subclass is defined.
"""

__author__ = 'Daniel'


class Meta(type):
    def __new__(mcs, name, bases, class_dict):
        """
        :param mcs:
        :param name: the name of the class
        :param bases: the parent classes it inherits from
        :param class_dict: all of the class attributes
        :return: Class
        """
        print (mcs, name, bases, class_dict)
        return type.__new__(mcs, name, bases, class_dict)


class MyClass(object):
    __metaclass__ = Meta
    foo = 1

    def __init__(self):
        self.bar = 2

    def foo_method(self):
        pass
