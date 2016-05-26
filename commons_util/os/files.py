import os
import re
import os.path as op
from shutil import copyfile
import shutil

__author__ = 'Danyang'


class FileUtils(object):
    @staticmethod
    def rename():
        """
        template
        :return:
        """
        find = r".+(?P<time>\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}\.png$)"
        dir = os.path.dirname(os.path.realpath(__file__))
        for r, dirs, fs in os.walk(dir):
            for f in fs:
                m = re.search(find, f)
                if m:
                    f1 = m.group("time")
                    os.rename(f, f1)
                    print "%s -> %s" % (f, f1)

    @staticmethod
    def abspath(dir, file):
        return op.abspath(os.path.join(dir, file))

    @staticmethod
    def toplevel_subdirs(dir):
        for item in os.listdir(dir):  # ls
            if os.path.isdir(os.path.join(dir, item)):  # -d
                yield item

    @staticmethod
    def cp(source, target):
        copyfile(source, target)

    @staticmethod
    def rmfile(path):
        os.remove(path)

    @staticmethod
    def rmdir(path):
        os.rmdir(path)

    @staticmethod
    def rmrf(path):
        shutil.rmtree(path)


class CmdUtils(object):
    @classmethod
    def execute(cls, cmd):
        os.system(cmd)