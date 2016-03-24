__author__ = 'Daniel'


class LazyDataStore(object):
    """
    data.__dict__
    hasattr(data, 'foo')
      hasattr will trigger __getattr__ if not present
    """
    def __init__(self):
        self.existing_attr = 5

    def __getattr__(self, name):
        """
        This method is called when the attribute is NOT present, i.e. accessing
        the missing attribute
        """
        value = 'Value for % s' % name
        setattr(self, name, value)
        return value


class LazyDataStore2(object):
    def __init__(self):
        self.existing_attr = 5

    def __getattribute__(self, name):
        """
        This special method is called EVERY time an attribute is accessed on an
        object, even in cases where it does exist in the attribute dictionary.
        """
        try:
            return super(LazyDataStore2, self).__getattribute__(name)
        except AttributeError:
            value = 'Value for %s' % name
            setattr(self, name, value)
            return value

    def __setattr__(self, name, value):
        """
        This method is always called every time an attribute is assigned on an
        instance
        """
        print "Aspect: Save some data to the DB log"
        super(LazyDataStore2, self).__setattr__(name, value)


class DictionaryDB(object):
    def __init__(self, data):
        self._data = data

    def __getattribute__(self, name):
        """
        To avoid infinite recursion in __getattribute__ and __setattr__ by using
        methods from super() (i.e., the object class) to access instance
        attributes directly.
        """
        _data = super(DictionaryDB, self).__getattribute__('_data')
        return _data[name]
