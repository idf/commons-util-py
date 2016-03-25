from unittest import TestCase
from util.commons_util.os.child_process import *
__author__ = 'Daniel'


class TestChildProcess(TestCase):
    def test_simple_exec(self):
        self.assertEquals(basic_child_process(),
            u'Hello from the child!\n')

    def test_poll_status(self):
        self.assertEquals(poll_status(), 'Exit status 0')
