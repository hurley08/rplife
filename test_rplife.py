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
    try:
        import rplife.patterns
        import rplife.grid
        import rplife.views
    except:
        assert False
    assert True


@pytest.fixture
def patterns():
    try:
        import rplife.patterns as patterns
    except Exception:
        assert False
    return patterns


@pytest.fixture
def get_pattern():
    from rplife.patterns import get_pattern
    return get_pattern


@pytest.fixture
def CursesView():
    from rplife.views import CursesView
    return CursesView


@pytest.fixture
def pytest_set():
    val_lits = patterns_set()
    val = ('test_pat', val_lits)
    return val


@pytest.fixture
def patterns_set():
    patterns_set = ['Pulsar', 'Beacon', 'Toad', 'Blinker']
    return patterns_set


def test_load_modules():
    try:
        from rplife.views import CursesView
        from rplife.patterns import Pattern
        from rplife.grid import LifeGrid
    except Exception:
        assert False
    assert True


@pytest.mark.parametrize('p_names', pat_name)
def test_lifegrid(get_pattern, patterns_set, p_names):
    from rplife.grid import LifeGrid
    p = LifeGrid(get_pattern(p_names))
    print(str(p))
    print(p.as_string)
    assert True


def test_get_all_patterns(patterns, get_pattern):
    result = patterns.get_all_patterns()
    assert (type(result) is list)
    assert (type(result[0]) != 'rplife.patterns.Pattern')


@pytest.mark.parametrize('p_name', pat_name)
def test_get_single_patterns(patterns, get_pattern, p_name):
    res = patterns.get_pattern(p_name)
    assert str(type(res)) == "<class 'rplife.patterns.Pattern'>"
    res = get_pattern(p_name)
    assert str(type(res)) == "<class 'rplife.patterns.Pattern'>"


def test_alive_cells_blinker(patterns):
    blink = patterns.get_pattern('Blinker')
    assert blink.alive_cells == {(2, 3), (2, 1), (2, 2)}


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
def test_cursesview_calls(CursesView, get_pattern, test_pattern):
    #    for i in patterns_set:
    d = CursesView(get_pattern(test_pattern)).show()
    assert d == False or d == None


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
def test_cursesview_rates(CursesView, get_pattern, patterns_set, f_rates):
    #   f_rates = [5, 25, 100, 500]
    for i in patterns_set:
        d = CursesView(get_pattern(i), frame_rate=f_rates).show()
        assert d == False or d == None


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
def test_cursesview_gen(CursesView, get_pattern, patterns_set, gens):
    #    f_rates = [5, 25, 100, 2000]
    for i in patterns_set:
        d = CursesView(get_pattern(i), frame_rate=200, gen=gens).show()
        assert d == False or d == None
