"""
Implements CursesVIew which uses curses to draw the states of patterns
"""
from __future__ import annotations

import curses
import sys
from time import sleep

from rplife.grid import LifeGrid
from rplife.patterns import Pattern


class CursesView:
    """
    Draws visuals of pattern in its current state
    """

    def __init__(
        self,
        pattern: Pattern,
        gen: int = 10,
        frame_rate: int = 20,
        bbox: tuple = (0, 0, 80, 80),
    ) -> None:
        """Initialize"""
        self.pattern = pattern
        self.gen = gen
        self.frame_rate = frame_rate
        self.bbox = bbox

    def show(self) -> bool:
        """Wraps _draw"""
        try:
            curses.wrapper(self._draw)
            return True

        except OSError as strerror:
            print(f'I/O error({strerror})')
        except ValueError:
            print('Could not convert data to an integer.')
        except:
            print('Unexpected error:', sys.exc_info()[0])
            raise
        return False

    def _draw(self, screen):
        """Draws a window with dimensions of bbox"""
        current_grid = LifeGrid(self.pattern)
        curses.curs_set(0)
        print(current_grid.as_string)
        try:
            screen.addstr(current_grid.as_string(self.bbox))
            print(f'Success in {self.bbox=}')
        except OSError as strerror:
            print(f'I/O error({strerror})')
            screen.refresh()
        except ValueError:
            print('Could not convert data to an integer.')
            screen.refresh()
        except curses.error as e:
            print(f"'Unexpected error:', sys.exc_info()[0] {e}")
            # screen.move(120,120)
            screen.refresh()
            print(current_grid.as_string((0, 0, 20, 20)))
            raise Exception(self.bbox, self.pattern.get_size())

        for _ in range(self.gen):
            try:
                current_grid.evolve()
                screen.addstr(current_grid.as_string(self.bbox))
                screen.refresh()
                sleep(1 / self.frame_rate)
            except:
                current_grid.evolve()
                screen.addstr(0, 0, current_grid.as_string(self.bbox))
                screen.refresh()
                sleep(1 / self.frame_rate)


__all__ = ['CursesView']
