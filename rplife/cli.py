"""
Implements a cli interface for rplife
"""
from __future__ import annotations

import argparse
try:
    from rplife import __version__, patterns, views
except:
    patterns, views, __version__ = False, False, False


def get_command_line_args():
    """ Get arguments and parameters"""
    if patterns:
        val = [pat.name for pat in patterns.get_all_patterns()]
    else:
        val = ['Blinker']
    if __version__:
        vers = f'%(prog)s v{__version__}'
    else:
        vers = True
    if views:
        vie = views.__all__
    else:
        vie = True
    parser = argparse.ArgumentParser(
        prog='rplife',
        description="Conway's Game of Life in your terminal",
    )

    parser.add_argument(
        '--version', action='version', version=vers,
    )
    parser.add_argument(
        '-p',
        '--pattern',
        choices=val,
        default='Blinker',
        help='take a pattern for the Game of Life (default: %(default)s)',
    )
    parser.add_argument(
        '-a',
        '--all',
        action='store_true',
        help='show all available patterns in a sequence',
    )
    parser.add_argument(
        '-v',
        '--view',
        choices=vie,
        default='CursesView',
        help='display the life grid in a specific view (default: %(default)s)',
    )
    parser.add_argument(
        '-g',
        '--gen',
        metavar='NUM_GENERATIONS',
        type=int,
        default=10,
        help='number of generations (default: %(default)s)',
    )
    parser.add_argument(
        '-f',
        '--fps',
        metavar='FRAMES_PER_SECOND',
        type=int,
        default=7,
        help='frames per second (default: %(default)s)',
    )
    print(parser)
    return parser.parse_args()
