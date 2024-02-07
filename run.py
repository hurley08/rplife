# pylint: skip-file
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

plat = get_pattern('Pulsar')
typus = get_pattern('Beacon')
duck = get_pattern('Toad')
plat.alive_cells = plat.alive_cells.union(typus.alive_cells)
plat.alive_cells = plat.alive_cells.union(duck.alive_cells)
# CursesView(plat, gen=250).show()
CursesView(get_pattern('Pulsar'), gen=10).show()
CursesView(get_pattern('Beacon'), gen=25).show()
CursesView(get_pattern('Toad'), gen=10).show()
