import patterns

o = patterns.get_all_patterns()

for i in o:
    t = max(i.alive_cells)
    if t[0] > t[1]:
        b = (t[0] * 3, t[0] * 3, 0, 0)
    else:
        b = (0, 0, t[1] * 3, t[1] * 3)
    import grid

    grid = grid.LifeGrid(i)
    print(grid.as_string((0, 0, 20, 20)))
    for i in range(200):
        grid.evolve()
        print(grid.as_string((0, 0, 20, 20)), end="/r", flush=True)
