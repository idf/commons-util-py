import copy_reg

__author__ = 'Daniel'


class State(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points


# Cannot be static method, class method
def pickle_state(instance):
    kwargs = instance.__dict__
    return unpickle_state, (kwargs,)

def unpickle_state(kwargs):
    return State(**kwargs)


copy_reg.pickle(State, pickle_state)