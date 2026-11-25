import pytest

'''def add(a, b):
    return a + b


def test_add():
    assert add(10, 20) == 30
    assert add(5, 5) == 10
    assert add(100, 200) == 300'''

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def test_add():
    assert add(10, 20) == 30


def test_subtract():
    assert subtract(20, 10) == 10


def test_multiply():
    assert multiply(5, 4) == 20


def test_divide():
    assert divide(20, 5) == 4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)