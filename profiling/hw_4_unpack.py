'''4. Распаковать вложенный список.'''
from functools import reduce
from itertools import chain
from operator import add
import random
from time import perf_counter

def extract_by_chain(list_of_lists: list):
    return list(chain.from_iterable(list_of_lists))

def extract_by_comprehension(list_of_lists: list):
    return [x for xlist in list_of_lists for x in xlist]

def extract_by_reduce(list_of_lists: list):
    return reduce(add, list_of_lists)

if __name__ == "__main__":
    x = [random.sample(range(1000), 1000) for _ in range(1000)]

    t_start = perf_counter()
    extract_by_chain(x)
    t_stop = perf_counter()
    print(f" extract list by chain ={t_stop - t_start}")

    t_start = perf_counter()
    extract_by_comprehension(x)
    t_stop = perf_counter()
    print(f" extract list by comprehension ={t_stop - t_start}")

    t_start = perf_counter()
    extract_by_reduce(x)
    t_stop = perf_counter()
    print(f" extract list by reduce ={t_stop - t_start}")

