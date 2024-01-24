"""
Implements Pattern which instantiates objects carrying information
to visualize and operate
"""
from __future__ import annotations

from typing import Any
from dataclasses import dataclass
from pathlib import Path


import tomllib

PATTERNS_FILE = Path(__file__).parent / "patterns.toml"


def get_pattern(
    name: str,
    filename: Path = PATTERNS_FILE,
) -> Pattern:
    """
    Retrieves a single pattern's parameters from file
    """
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return Pattern.from_toml(name, toml_data=data[name])


def get_all_patterns(
    filename: Path = PATTERNS_FILE,
) -> list:
    """ "
    Retrieves all patterns and stores in a dict
    """
    data = tomllib.loads(filename.read_text(encoding="utf-8"))
    return [Pattern.from_toml(name, toml_data) for name, toml_data in data.items()]


@dataclass
class Pattern:
    """
    Accepts name and live cells, returns Pattern object
    """

    name: str
    alive_cells: set[tuple[int, int]]

    @classmethod
    def from_toml(cls, name: str, toml_data: Any):
        """
        Maps live cells of target pattern
        """
        return cls(
            name,
            alive_cells={tuple(cell) for cell in toml_data["alive_cells"]},
        )
