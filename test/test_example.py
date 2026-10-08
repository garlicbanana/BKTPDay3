from src.my_math import add_numbers

from src.my_math import subtract_numbers

from src.my_math import multiply_numbers

def test_add_numbers():
    assert add_numbers(1, 3) == 4

def test_subtract_numbers():
    assert subtract_numbers(3, 2) == 1

def test_multiply_numbers():
    assert multiply_numbers(5, 3) == 15
