from __future__ import annotations

import pytest


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
def patterns_set():
    return ['Pulsar', 'Beacon', 'Toad', 'Blinker']


def test_load_modules():
    try:
        from rplife.views import CursesView
        from rplife.patterns import Pattern
        from rplife.grid import LifeGrid
    except Exception:
        assert False
    assert True


def test_get_all_patterns(patterns, get_pattern):
    result = patterns.get_all_patterns()
    assert (type(result) is list)
    assert (type(result[0]) != 'rplife.patterns.Pattern')


def test_get_single_patterns(patterns, get_pattern, patterns_set):
    for i in patterns_set:
        res = patterns.get_pattern(i)
        assert str(type(res)) == "<class 'rplife.patterns.Pattern'>"
    for i in patterns_set:
        res = get_pattern(i)
        assert str(type(res)) == "<class 'rplife.patterns.Pattern'>"
    assert True


def test_alive_cells_blinker(patterns):
    blink = patterns.get_pattern('Blinker')
    assert blink.alive_cells == {(2, 3), (2, 1), (2, 2)}


def test_cursesview_calls(CursesView, get_pattern, patterns_set):
    for i in patterns_set:
        d = CursesView(get_pattern(i)).show()
        assert d == False or d == None


def test_cursesview_rates(CursesView, get_pattern, patterns_set):
    f_rates = [5, 25, 100, 500]
    for i in patterns_set:
        for j in f_rates:
            d = CursesView(get_pattern(i), frame_rate=j).show()
            assert d == False or d == None


def test_cursesview_gen(CursesView, get_pattern, patterns_set):
    f_rates = [5, 25, 100, 2000]
    for i in patterns_set:
        for j in f_rates:
            d = CursesView(get_pattern(i), frame_rate=200, gen=j).show()
            assert d == False or d == None
