"""Найдите все четные числа из списка VALUES тремя способами """
from itertools import chain
from typing import Generator, List

VALUES = [
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]],
    [[28, 29, 30], [31, 32, 33], [34, 35, 36]],
]


def get_even_for_loop(values: List) -> List[int]:
    """Return all even numbers using classical for loop.
    :param values: input list of lists with values
    :return: list with int values
    """
    result = list()
    for value in values:
        for val in value:
            for v in val:
                if v % 2 == 0:
                    result.append(v)
    return result


def get_even_for_loop_iterator(values: List) -> Generator:
    """Return all even numbers using classical for loop.
    :param values: input list of lists with values
    :return: generator with int values
    """
    for value in values:
        for val in value:
            for v in val:
                if v % 2 == 0:
                    yield v


def get_even_list_comprehension(values: List) -> List[int]:
    """Return all even numbers in ONE LINE using list comprehension.
    :param values: input list of lists with values
    :return: list with int values
    """
    return [c for a in values for b in a for c in b if c % 2 == 0]
   # return list(
   #     x for x in chain.from_iterable(chain.from_iterable(values)) if x % 2 == 0
   # )


print(get_even_for_loop(VALUES))
print(list(get_even_for_loop_iterator(VALUES)))
print(get_even_list_comprehension(VALUES))

# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
