__author__ = 'Daniel'


def _add_tests(generator):
    """
    http://stackoverflow.com/questions/2798956/python-unittest-generate-multiple-tests-programmatically#answer-2799482
    """
    def class_decorator(cls):
        """Add tests to `cls` generated by `generator()`."""
        for f, args in generator():
            # closure in python is lexical rather than dynamic
            test = lambda self, args=args, f=f: f(self, *args)

            test.__name__ = "test_%s_%s" % (f.__name__, args[0])
            setattr(cls, test.__name__, test)
        return cls

    return class_decorator