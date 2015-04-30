__author__ = 'Daniel'


class Image(object):
    """
    ref:
    http://tech.oyster.com/save-ram-with-python-slots/
    """
    def __init__(self, id, caption, url):
        self.id = id
        self.caption = caption
        self.url = url

    # ... other methods ...


class Image(object):
    """
    For small classes that have a few fixed attributes known at "compile time", the dict is a waste of RAM
    You can tell Python not to use a dict, and only allocate space for a fixed set of attributes, by settings __slots__
    on the class to a fixed list of attribute names

    Cautious notes:  Don't prematurely optimize and use this everywhere! It's not great for code maintenance, and it
    really only saves you when you have thousands of instances.
    """
    __slots__ = ['id', 'caption', 'url']

    def __init__(self, id, caption, url):
        self.id = id
        self.caption = caption
        self.url = url

    # ... other methods ...