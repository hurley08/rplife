# rplife/run.py
from __future__ import annotations

from rplife import patterns
from rplife.patterns import get_pattern
from rplife.views import CursesView
# import patterns
# from rplife import patterns#
# from patterns import get_pattern


patterns.get_pattern('Blinker')
# Pattern(name='Blinker', alive_cells={(2,3)})


patterns.get_all_patterns()


CursesView(get_pattern('Glider Gun'), gen=100).show()
