""" Classes Advanced HomeWork"""
import functools
from abc import ABC, abstractmethod


@functools.total_ordering
class Currency(ABC):
    """1 EUR == 2 USD == 100 RUB"""

    def __init__(self, value):
        self.value = value

    @property
    @staticmethod
    @abstractmethod
    def name():
        pass

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if val < 0:
            raise ValueError("Value cannot be negative")
        self._value = val

    def to(self, currency):
        return currency(self.value * self.course_v(currency))

    def __eq__(self, other):
        if type(self) == type(other):
            return self.value == other.value
        if isinstance(other, Currency):
            return self == other.to(type(self))
        return super().__eq__(other)

    def __lt__(self, other):
        if type(self) == type(other):
            return self.value < other.value
        if isinstance(other, Currency):
            return self < other.to(type(self))
        return super().__lt__(other)

    def __add__(self, other):
        if type(self) == type(other):
            return type(self)(self.value + other.value)
        if isinstance(other, Currency):
            return self + other.to(type(self))
        return super().__add__(other)

    def __radd__(self, other):
        if isinstance(other, int):
            return type(self)(other + self.value)
        return super().__radd__(other)

    def __repr__(self):
        return f"{self.value} {self.name}"

    @staticmethod
    @abstractmethod
    def course_v(currency: type) -> int:
        pass

    @staticmethod
    @abstractmethod
    def course(currency: type) -> str:
        pass


class Euro(Currency):
    """1 EUR == 2 USD == 100 RUB"""

    name = "EUR"

    @staticmethod
    def course_v(currency: type):
        return {Euro: 1, Dollar: 2, Rubble: 100,}[currency]

    @staticmethod
    def course(currency: type):
        """100.0 RUB for 1 EUR"""
        return f"{Euro.course_v(currency)} {currency.name} for 1 {Euro.name}"


class Dollar(Currency):
    """1 EUR == 2 USD"""

    name = "USD"

    @staticmethod
    def course_v(currency: type):
        return {
            Euro: 1 / Euro.course_v(Dollar),
            Dollar: 1,
            Rubble: Euro.course_v(Rubble) / Euro.course_v(Dollar),
        }[currency]

    @staticmethod
    def course(currency: type):
        return f"{Dollar.course_v(currency)} {currency.name} for 1 {Dollar.name}"


class Rubble(Currency):
    """1 EUR ==  100 RUB"""

    name = "RUB"

    @staticmethod
    def course_v(currency: type):
        return {
            Euro: 1 / Euro.course_v(Rubble),
            Dollar: Euro.course_v(Dollar) / Euro.course_v(Rubble),
            Rubble: 1,
        }[currency]

    @staticmethod
    def course(currency: type):
        return f"{Rubble.course_v(currency)} {currency.name} for 1 {Rubble.name}"


print(
    f"Euro.course(Rubble)   ==> {Euro.course(Rubble)}\n"
    f"Dollar.course(Rubble) ==> {Dollar.course(Rubble)}\n"
    f"Rubble.course(Euro)   ==> {Rubble.course(Euro)}\n"
)

e = Euro(100)
r = Rubble(100)
d = Dollar(200)

print(
    f"e = {e}\n"
    f"e.to(Dollar) ==> {e.to(Dollar)}\n"
    f"e.to(Rubble) ==> {e.to(Rubble)}\n"
    f"e.to(Euro)   ==> {e.to(Euro)}\n"
)
print(
    f"r = {r}\n"
    f"r.to(Dollar) ==> {r.to(Dollar)}\n"
    f"r.to(Euro)   ==> {r.to(Euro)}\n"
    f"r.to(Rubble) ==> {r.to(Rubble)}\n"
)

print(f"e > r  ==> {e > r}\n" f"e == d ==> {e == d}\n")

print(f"e + r  =>  {e + r}\n" f"r + d  =>  {r + d}\n" f"d + e  =>  {d + e}\n")

print(sum([Euro(i) for i in range(5)]))
