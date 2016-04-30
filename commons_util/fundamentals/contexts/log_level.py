from contextlib import contextmanager
import logging


__author__ = 'Daniel'


@contextmanager
def debug_logging(level):
    """
    Set the log level temporarily

    Usage:
      # default normally logging.WARNING
      with debug_logging(logging.DEBUG):
          logging.debug('debug log')

    yied:
      The yield expression is the point at which the with block's contents will
      execute. Any exceptions that happen in the with block will be re-raised
      by the yield expression
    :param level: logging level
    :return: context
    """
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)


@contextmanager
def log_level(level, name):
    """
    Returns a logger with `name` with `level`

    Usage:


    :param level: logging level
    :param name: str
    :return: logger
    """
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)