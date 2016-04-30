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
from concurrent.futures import ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def threading():
    """
    ProcessPoolExecutor
    1. It takes each item from the numbers input data to map.
    2. It **serializes** it into binary data using the pickle module
    3. It copies the serialized data from the main interpreter process to a
    child interpreter process over a local **socket**.
    4. Next, it deserializes the data back into Python objects using pickle in
    the child process.
    5. It then imports the Python module containing the gcd function.
    6. It runs the function on the input data in parallel with other child
    processes.
    7. It serializes the result back into bytes.
    8. It copies those bytes back through the socket.
    9. It deserializes the bytes back into Python objects in the parent
    process.
    10. Finally, it merges the results from multiple children into a single
    list to return.
    :return:
    """
    numbers = [(1963309, 2265973), (2030677, 3814172),
               (1551645, 2229620), (2039045, 2020802)]
    pool = ProcessPoolExecutor(max_workers=2)
    ret = list(pool.map(gcd, numbers))
    return ret
