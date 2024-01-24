"""
 Entry point
"""
from __future__ import annotations

import sys

from rplife import patterns
from rplife import views
from rplife.cli import get_command_line_args

o = patterns.get_all_patterns()

for i in o:
    t = max(i.alive_cells)
    if t[0] > t[1]:
        b = (t[0] * 3, t[0] * 3, 0, 0)
    else:
        b = (0, 0, t[1] * 3, t[1] * 3)
    from rplife import grid

    gridl = grid.LifeGrid(i)
    for i in range(200):
        gridl.evolve()
        print(gridl.as_string((0, 0, 20, 20)), end='/r', flush=True)


def _show_pattern(View, patter, args):
    """
     Wrapper to handle any exceptions while stepping through generations
    """
    try:
        View(pattern=patter, gen=args.gen, frame_rate=args.fps).show()
    except OSError as strerror:
        print(f'I/O error({strerror}):')
    except ValueError:
        print('Could not convert data to an integer.')
    except:
        print('Unexpected error:', sys.exc_info()[0])
        raise


def main():
    """
     Entry Point for rplife
    """
    args = get_command_line_args()
    View = getattr(views, args.view)
    if args.all:
        for pattern in patterns.get_all_patterns():
            _show_pattern(View, pattern, args)
    else:
        _show_pattern(
            View,
            patterns.get_pattern(name=args.pattern),
            args,
        )
