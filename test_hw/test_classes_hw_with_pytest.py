import pytest
from test_hw.classes_adv_hw import Euro, Rubble, Dollar


def test_convert_course_positive():
    assert Euro.course(Rubble) == '100 RUB for 1 EUR'
    assert Dollar.course(Rubble) == '50.0 RUB for 1 USD'
    assert Rubble.course(Euro) == '0.01 EUR for 1 RUB'

def test_convert_course_negative():
    with pytest.raises(ValueError) as e:
        Euro.course(-1)

    assert str(e.value) == 'Currency class required', \
        'Wrong exception was raised'

def  test_convert_to_positive():
    e =  Euro(100)
    assert e.to(Dollar) == Dollar(200)
    assert e.to(Rubble) == Rubble(10000)
    assert e.to(Euro) == Euro(100)

def test_print_positive():
    e = Euro(100)
    r = Rubble(100)
    d = Dollar(200)
    assert e.__str__() == '100 EUR'
    assert r.__str__() == '100 RUB'
    assert d.__str__() == '200 USD'

def test_compare_positive():
    e = Euro(100)
    r = Rubble(100)
    d = Dollar(200)
    assert e > r
    assert e == d

def test_add_positive():
    e = Euro(100)
    r = Rubble(100)
    d = Dollar(200)
    assert e + r == Euro(101)
    assert r + d == Rubble(10100)
    assert d + e == Dollar(400)


def test_sum_positive():
    assert sum([Euro(i) for i in range(5)]) == Euro(10)
