"""
This is a test
"""
# rplife/run.py
from __future__ import annotations

import sys

try:
    from rplife import patterns
    from rplife.patterns import get_pattern
    from rplife.views import CursesView
except IOError as (errno, strerror):
    print('I/O error({}): {}'.format(errno, strerror))
except ValueError:
    print('Could not convert data to an integer.')
except:
    print('Unexpected error:', sys.exc_info()[0])
    raise
    # import patterns
    # from rplife import patterns#
    # from patterns import get_pattern
    # from views import CursesView
    raise Exception('Something failed') from e

patterns.get_pattern('Blinker')
# Pattern(name='Blinker', alive_cells={(2,3)})


patterns.get_all_patterns()


print(CursesView(get_pattern('Pulsar'), gen=100).show())
