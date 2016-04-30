from functools import wraps
from util.commons_util.logger.Timer import Timer

__author__ = 'Danyang'


def timestamp(func):
    """
    time the execution time of a function

    :param func: the function, whose result you would like to cached based on input arguments
    """
    def ret(*args):
        timer = Timer()
        timer.start()
        result = func(*args)
        print timer.end()
        return result
    return ret


def print_func_name(func):
    """
    print the current executing function name
    possible use:
    >>> print sys._getframe().f_code.co_name
    :param func: the function, whose result you would like to cached based on input arguments
    """
    def wrapper(*args):
        print func.func_name
        result = func(*args)
        return result
    return wrapper


def trace(func):
    """
    print calling information
    e.g. f(a, b) -> y

    Usage:
    @trace
    def f(a, b):
        ...

    Issue:
      with naive decoration, the func's name will change from outside view.
      Using decorators can cause strange behaviors in tools that do
      introspection, such as debuggers.
    Solution:
      Applying it to the wrapper function @wraps(func) will copy all of the
      important metadata about the inner function to the outer function.
    :param func:
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('%s(%r, %r) -> %r' %
              (func.__name__, args, kwargs, result))
        return result

    return wrapper
