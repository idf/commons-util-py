import abc
from weakref import WeakKeyDictionary
import six

__author__ = 'Daniel'


class Shape(object):
    __metaclass__ = abc.ABCMeta  # Abstract Base Class

    @abc.abstractmethod
    def method_to_implement(self, i):
        """
        Method documentation
        Replace: raise NotImplementedError("This method not implemented")
        """
        return


# Property
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


# Descriptor
class GradeDescriptor(object):
    def __init__(self):
        self._values = WeakKeyDictionary()
        # gc when holding the instance's last remaining reference

    def __get__(self, instance, instance_type):
        """
        e.g. print obj.grade
        """
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        """
        e.g. obj.grade = 1
        """
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value


## Descriptor and ORM model
class NaiveModelField(object):
    """
    Descriptor using getattr and setattr
    instance dictionary rather than WeakKeyDictionary()

    Usage:
    ```
    class Customer(object):
        first_name = NaiveModelField('first_name')
    ```
    Redundancy: need to specify the name of the class attribute.

    This NaiveModelField class will be replaced by meta class.
    """
    def __init__(self, name):
        self.name = name
        self.internal_name = '_' + self.name

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class ModelField(object):
    """
    Improvement
    Usage:
    ```
    class Customer(Model):
        first_name = ModelField()
    ```
    """
    def __init__(self):
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None: return self
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        setattr(instance, self.internal_name, value)


class ModelBaseMeta(type):
    def __new__(mcs, name, bases, class_dict):
        for key, value in class_dict.items():
            if isinstance(value, ModelField):
                value.name = key
                value.internal_name = '_' + key

        cls = type.__new__(mcs, name, bases, class_dict)
        return cls


class Model(six.with_metaclass(ModelBaseMeta)):
    pass