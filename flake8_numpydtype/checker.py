from .version import __version__
from ast import walk, Call, Name, List, Attribute

NPT010 = "NPT010 "

class NumpyDTypeChecker(object):
    name = 'flake8_numpydtype'
    version = __version__

    def __init__(self, tree):
        self.tree = tree

    def run(self):
        for node in walk(self.tree):
            if not isinstance(node, Name):
                continue
            print(node)
            '''
            if isinstance(node.func, Name) and node.func.id in ('sorted',):
                flake8warn = STC010
            elif isinstance(node.func, Attribute) and isinstance(node.func.value, (Name, Attribute, List)) and node.func.attr in ('sort',):
                flake8warn = STC011
            else:
                continue

            if any(keyword.arg == 'cmp' for keyword in node.keywords):
                yield node.lineno, node.col_offset, flake8warn, type(self)
            '''
