"""
Tests for calculator core functionality.
"""


import pytest
import sys
import os


from src.calculator_api.core import add, subtract, multiply, divide
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))


class TestAdd:
    """Test cases for add function."""

    def test_add_positive_numbers(self):
        """Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 5) == 15

    def test_add_negative_numbers(self):
        """Test adding negative numbers."""
        assert add(-1, -1) == -2
        assert add(-5, 3) == -2

    def test_add_zero(self):
        """Test adding with zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0


class TestSubtract:
    """Test cases for subtract function."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        assert subtract(5, 3) == 2
        assert subtract(10, 2) == 8

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        assert subtract(5, -3) == 8
        assert subtract(-5, -3) == -2


class TestMultiply:
    """Test cases for multiply function."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        assert multiply(2, 3) == 6
        assert multiply(5, 4) == 20

    def test_multiply_by_zero(self):
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        assert multiply(-2, 3) == -6
        assert multiply(2, -3) == -6
        assert multiply(-2, -3) == 6


class TestDivide:
    """Test cases for divide function."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        assert divide(10, 2) == 5.0
        assert divide(9, 3) == 3.0

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0

    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(10, 0)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0.0
