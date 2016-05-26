import importlib
import inspect
import sys
import os.path as op
__author__ = 'Daniel'


class Importer(object):
    @staticmethod
    def import_module(path):
        # path -> basename -> strip extension
        sys.path.append(op.dirname(path))
        file_name = op.splitext(op.basename(path))[0]
        return importlib.import_module(file_name)

    @staticmethod
    def inspect_module_classes(path):
        module = Importer.import_module(path)
        return [(name, module) for name, obj in inspect.getmembers(module)
                if inspect.isclass(obj)  # filter only classes
        ]
