from unittest import TestCase
import multiprocessing as mp
import random
import string

__author__ = 'Danyang'


class TestCounter(TestCase):
    def test_increment(self):
        pass

    def test_value(self):
        pass


def cube(x):
    """
    Cannot be a class method: The problem is that multiprocessing must pickle things to sling them among processes, and
    bound methods are not picklable. The workaround (whether you consider it "easy" or not;-) is to add the
    infrastructure to your program to allow such methods to be pickled, registering it with the copy_reg standard
    library method.
    """
    return x**3


class TestMp(TestCase):
    """
    Based on:
    http://sebastianraschka.com/Articles/2014_multiprocessing_intro.html
    """
    def rand_string(self, length, output):
        """
        Generates a random string of numbers, lower- and uppercase chars.
        """
        rand_str = ''.join(random.choice(
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits) for _ in range(length))

        output.put(rand_str)

    def test_generate_random_str(self):
        """
        Simple way of multi-processing
        :return:
        """
        # Define an output queue
        output = mp.Queue()

        # Setup a list of processes that we want to run
        processes = [mp.Process(target=self.rand_string, args=(5, output)) for x in range(4)]

        # Run processes
        for p in processes:
            p.start()

        # Exit the completed processes
        for p in processes:
            p.join()

        # Get process results from the output queue
        results = [output.get() for p in processes]

        self.assertEqual(len(results), 4)
        self.assertTrue(all(map(lambda x: len(x)==5, results)))

    def test_pool(self):
        """
        * Pool.apply
        * Pool.map
        * Pool.apply_async
        * Pool.map_async
        """
        expected = [1, 8, 27, 64, 125, 216]
        pool = mp.Pool(processes=4)
        results = [pool.apply(cube, args=(x,)) for x in range(1, 7)]
        self.assertEqual(results, expected)

        pool = mp.Pool(processes=4)
        results = pool.map(cube, range(1, 7))
        self.assertEqual(results, expected)

        pool = mp.Pool(processes=4)
        results = [pool.apply_async(cube, args=(x,)) for x in range(1, 7)]
        output = [p.get() for p in results]
        self.assertEqual(output, expected)