# rplife/run.py
from __future__ import annotations
try:
    from rplife import patterns
    from rplife.patterns import get_pattern
    from rplife.views import CursesView
except Exception:
    # import patterns
    # from rplife import patterns#
    # from patterns import get_pattern
    # from views import CursesView
    raise (Exception('Something failed'))

patterns.get_pattern('Blinker')
# Pattern(name='Blinker', alive_cells={(2,3)})


patterns.get_all_patterns()


print(CursesView(get_pattern('Pulsar'), gen=100).show())
