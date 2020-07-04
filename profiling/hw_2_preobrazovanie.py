"""
Домашнее задание
2. К каждому элементу списка применить какуе-либо преобразование (например, для числового списка - возвести в кавдрат,
 для строкового - привести к верхнему регистру, отфильтровать определенные символы, и т.д.).
"""

import random
import string
from time import perf_counter


def squared_append(x: list):
    y = list()
    for i in x:
        y.append(i * i)
    return y


def squared_map(x: list):
    return map(lambda i: i * i, x)


def squared_comrehension(x: list):
    return [i * i for i in x]


def upper_append(x: list):
    y = list()
    for i in x:
        y.append(i.upper())
    return y


def upper_map(x: list):
    return map(lambda i: i.upper(), x)


def upper_comprehension(x: list):
    return [i.upper() for i in x]


def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(stringLength))


if __name__ == "__main__":
    x = range(1_000_000)

    # для числового списка - возвести в кавдрат
    t_start = perf_counter()
    squared_append(x)
    t_stop = perf_counter()
    print(f" squared list by appending ={t_stop - t_start}")

    t_start = perf_counter()
    squared_map(x)
    t_stop = perf_counter()
    print(f" squared list by mapping ={t_stop - t_start}")

    t_start = perf_counter()
    squared_comrehension(x)
    t_stop = perf_counter()
    print(f" squared list by comrehension ={t_stop - t_start}")

    # для строкового - привести к верхнему регистру
    x = [randomString() for _ in range(1_000_000)]

    t_start = perf_counter()
    upper_append(x)
    t_stop = perf_counter()
    print(f" uppercase for list by appending ={t_stop - t_start}")

    t_start = perf_counter()
    upper_map(x)
    t_stop = perf_counter()
    print(f" uppercase for list by map ={t_stop - t_start}")

    t_start = perf_counter()
    upper_comprehension(x)
    t_stop = perf_counter()
    print(f" uppercase for list by comrehension ={t_stop - t_start}")
