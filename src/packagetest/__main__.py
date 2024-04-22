# __main__.py
print(f"__main__.py: __name__={repr(__name__)}")

import collections
import os
import sys

# Update sys.path and remove duplicate entries.
sys.path.insert(1, os.path.dirname(os.path.realpath(__file__)))
unique_path = list(collections.OrderedDict.fromkeys(sys.path))
# print(repr(sys.path), repr(unique_path), sep='\n')
sys.path = unique_path

from __init__ import main

"""Include if __name__ == '__main': code from __init__.py"""
# Check whether imported in an IDE.
is_idle, is_pycharm, is_jupyter = (
    'idlelib' in sys.modules,
    int(os.getenv('PYCHARM', 0)),
    '__file__' not in globals()
)
if any((is_idle, is_pycharm, is_jupyter,)):
    tests = [
        [ 'packagetest.py', '-?', ],
    ]
    for test in tests:
        main(test)
else:
    sys.exit(main(sys.argv))
