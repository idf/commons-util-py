import abc
from weakref import WeakKeyDictionary

__author__ = 'Daniel'


class Shape(object):
    __metaclass__ = abc.ABCMeta  # Abstract Base Class

    @abc.abstractmethod
    def method_to_implement(self, input):
        """
        Method documentation
        Replace: raise NotImplementedError("This method not implemented")
        """
        return


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


class VoltageResistance(Resistor):
    """Usage of @property"""
    def __init__(self, ohms):
        super(VoltageResistance, self).__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


class GradeDescriptor(object):
    def __init__(self):
        self._values = WeakKeyDictionary()
        # gc when holding the instance's last remaining reference

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value