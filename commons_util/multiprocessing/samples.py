"""
General concepts in python concurrency

GIL: Global interpreter lock. At ANY time, only ONE BYTECODE is interpreted by
the Python interpreter.

* multithreading module is for IO intensive tasks.
* multiprocessing module is for CPU intensive tasks, with pickle as var
sharing.
"""
__author__ = 'Daniel'

# multi processing
from multiprocessing import Pool
# multi threading; used for testing the efficacy of multiprocessing
from multiprocessing.dummy import Pool