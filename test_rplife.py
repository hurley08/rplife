# pylint: skip-file
# rplife/test_rplife.py
"""
    pytest suite
"""
from __future__ import annotations

import pytest


pat_name = [
    'Blinker',
    'Toad',
    'Pulsar',
    'Beacon',
    'Bunnies',
    'Glider',
    'Glider Gun',
]


def test_imports():
    """Test import x.y pattern"""
    try:
        import rplife.grid
        import rplife.views
    except Exception:
        assert False
    print(rplife.views)
    """To suppress not used error"""
    assert True


@pytest.fixture
def patterns():
    """Import patterns module for later use"""
    try:
        import rplife.patterns as patterns
    except Exception:
        assert False
    return patterns


@pytest.fixture
def get_pattern():
    """Imports get_pattern() method for later use"""
    from rplife.patterns import get_pattern
    return get_pattern


@pytest.fixture
def curses_view():
    """Imports CursesView() class for later use"""
    from rplife.views import CursesView
    return CursesView


@pytest.fixture
def pytest_set():
    """Turn list of patterns into parametrized format"""
    val = ('test_pat', pat_name)
    return val


@pytest.fixture
def patterns_set():
    """Turn list of pattern names into fixture"""
    patterns_set = pat_name
    return patterns_set


def test_load_modules():
    """Import using from x import x.y format"""
    try:
        from rplife.views import CursesView
        from rplife.patterns import Pattern
        from rplife.grid import LifeGrid
    except Exception:
        assert False
    print(CursesView, Pattern, LifeGrid)
    assert True


@pytest.mark.parametrize('p_names', pat_name)
def test_lifegrid(get_pattern, patterns_set, p_names):
    """
    Use LifeGrid to create Pattern objects given name
    and alive cells attributes
    """
    from rplife.grid import LifeGrid
    p = LifeGrid(get_pattern(p_names))
    print(str(p))
    print(p.as_string)
    assert True


def test_get_all_patterns(patterns, get_pattern):
    """use get_pattern method, check the resulting list for type"""
    from rplife.patterns import Pattern
    result = patterns.get_all_patterns()
    assert isinstance(result, list)
    assert isinstance(result[0], Pattern)

    # assert (type(result) is list)
    # assert (type(result[0]) != 'rplife.patterns.Pattern')


@pytest.mark.parametrize('p_name', pat_name)
def test_get_single_patterns(patterns, get_pattern, p_name):
    """use two different import methods to get_pattern a list of patterns"""
    from rplife.patterns import Pattern
    res = patterns.get_pattern(p_name)
    assert isinstance(res,  Pattern)
    # assert str(type(res)) == "<class 'rplife.patterns.Pattern'>"
    res = get_pattern(p_name)
    assert isinstance(res,  Pattern)
    # assert str(type(res)) == "<class 'rplife.patterns.Pattern'>"


def test_alive_cells_blinker(patterns):
    """get pattern, test presence of alive_cells attribute"""
    blink = patterns.get_pattern('Blinker')
    assert blink.alive_cells == {(2, 3), (2, 1), (2, 2)}


@pytest.mark.xfail
@pytest.mark.parametrize(
    'test_pattern',
    [
        'Blinker',
        'Toad',
        'Pulsar',
        'Beacon',
        'Bunnies',
        'Glider',
        'Glider Gun',
    ],
)
def test_cursesview_calls(curses_view, get_pattern, test_pattern):
    """get pattern, execute CursesView.show()"""
    d = curses_view(get_pattern(test_pattern)).show()
    assert d in (False, None)


@pytest.mark.xfail
@pytest.mark.parametrize(
    'f_rates',
    [
        5,
        25,
        100,
        500,
        1000,
    ],
)
def test_cursesview_rates(curses_view, get_pattern, patterns_set, f_rates):
    """Tests CursesView.show() with a range frame rates"""
    for i in patterns_set:
        d = curses_view(get_pattern(i), frame_rate=f_rates).show()
        assert d in (False, None)


@pytest.mark.xfail
@pytest.mark.parametrize(
    'gens',
    [
        5,
        25,
        100,
        1000,
        2000,
    ],
)
def test_cursesview_gen(curses_view, get_pattern, patterns_set, gens):
    """Uses values in gens, tests number of generations"""
    for i in patterns_set:
        d = curses_view(get_pattern(i), frame_rate=200, gen=gens).show()
        assert d in (False, None)
