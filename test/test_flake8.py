from sys import version_info
from pytest import mark
from ast import parse
from flake8_numpydtype.checker import NumpyDTypeChecker

def test_positive_bool():
    tree = parse('''
import numpy
numpy.bool_
''')
    violations = list(NumpyDTypeChecker(tree).run())
    assert len(violations) == 0

def test_bool():
    tree = parse('''
import numpy
numpy.bool
''')
    violations = list(NumpyDTypeChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('NPT010 ')

def test_bool_importas():
    tree = parse('''
import numpy as np
np.bool
''')
    violations = list(SortcmpChecker(tree).run())
    assert len(violations) == 1
    assert violations[0][2].startswith('NPT010 ')

