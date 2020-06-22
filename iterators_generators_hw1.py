def CustomZip(*args):
    m = min(len(arg) for arg in args)
    for i in range(0, m):
      yield tuple(arg[i] for arg in args)

list(CustomZip(['A', 'B', 'C'], [1, 2, 3], (22, 33, 44, 55, 66)))