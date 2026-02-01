import pytest
from app.operations import addition, subtraction, multiplication, division

def test_addition():
   assert addition(1, 1) == 2

def test_subtraction():
   assert subtraction(5, 3) == 2

def test_multiplication():
    assert multiplication(2, 3) == 6

def test_division():
    assert division(8, 2) == 4

def test_division_by_zero():
    with pytest.raises(ValueError) as excinfo:
        division(5, 0)
    assert str(excinfo.value) == "Error: Division by zero is not allowed."

def test_division_negative():
    assert division(-6, 2) == -3

def test_addition_negative():
    assert addition(-1, -1) == -2

def test_subtraction_negative():
    assert subtraction(-5, -3) == -2
