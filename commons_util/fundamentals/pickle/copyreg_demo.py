import copy_reg

__author__ = 'Daniel'


class State(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points

    @classmethod
    def pickle(cls, instance):
        kwargs = instance.__dict__
        return cls.unpickle, (kwargs,)

    @classmethod
    def unpickle(cls, kwargs):
        return cls(**kwargs)


copy_reg.pickle(State, State.pickle)