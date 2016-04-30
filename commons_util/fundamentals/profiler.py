from cProfile import Profile
from pstats import Stats


__author__ = 'Daniel'


def demo():
    """
    more one https://pymotw.com/2/profile/
    :return:
    """
    f = lambda x: x

    profiler = Profile()
    profiler.runcall(f)  # run the target function

    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    # table of information organized by function
    stats.print_stats()

    # Caller / Callee Graphs
    # seeing which callers contributed to the profiling information of each
    # function
    stats.print_callers()
    stats.print_callees()
