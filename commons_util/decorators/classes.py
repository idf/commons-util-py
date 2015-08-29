import warnings
import functools
__author__ = 'Danyang'


def Override(interface_class):
    """
    provide java-like @Override annotation
    usage: @Override(Interface) as method annotation
    :param interface_class: Class
    :exception: AssertionError
    :return: method
    """
    def overrider(method):
        try:
            assert (method.__name__ in dir(interface_class))
            return method
        except AssertionError:
            print method.__name__+" for "+interface_class.__name__

    return overrider


warnings.simplefilter('always', DeprecationWarning)


def Deprecated(func, msg=None):
    """
    provide java-like @Deprecated annotation
    A decorator which can be used to mark functions
    as deprecated.It will result in a deprecation warning being shown
    when the function is used.
    :param func: the function decorated
    :param msg: message issued when warning deprecating
    """
    message = msg or "Use of deprecated function '{}`.".format(func.__name__)

    @functools.wraps(func)
    def wrapper_func(*args, **kwargs):
        warnings.warn(message, DeprecationWarning, stacklevel=2)
        return func(*args, **kwargs)

    return wrapper_func


def method_decorator(decorator):
    """
    Adapted from Django
    Converts a function decorator into a method decorator
    """
    # 'func' is a function at the time it is passed to _dec, but will eventually
    # be a method of the class it is defined on.
    def _dec(func):
        def _wrapper(self, *args, **kwargs):
            @decorator
            def bound_func(*args2, **kwargs2):
                return func.__get__(self, type(self))(*args2, **kwargs2)
            # bound_func has the signature that 'decorator' expects i.e.  no
            # 'self' argument, but it is a closure over self so it can call
            # 'func' correctly.
            return bound_func(*args, **kwargs)
        # In case 'decorator' adds attributes to the function it decorates, we
        # want to copy those. We don't have access to bound_func in this scope,
        # but we can cheat by using it on a dummy function.

        @decorator
        def dummy(*args, **kwargs):
            pass
        functools.update_wrapper(_wrapper, dummy)
        # Need to preserve any existing attributes of 'func', including the name.
        functools.update_wrapper(_wrapper, func)

        return _wrapper