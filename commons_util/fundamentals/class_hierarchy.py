import abc

__author__ = 'Daniel'


class Shape(object):
    __metaclass__ = abc.ABCMeta  # Abstract Base Class 

    @abc.abstractmethod
    def method_to_implement(self, input):
        """Method documentation"""
        return