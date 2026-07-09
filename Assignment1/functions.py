"""
This module contains simple Python functions:
1. Add two numbers.
2. Check if a number is even.
3. Find the larger of two numbers.
"""


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


result = add_numbers(10, 20)
print("Sum =", result)


def check_even(number):
    """Return True if the number is even, otherwise False."""
    return number % 2 == 0


print(check_even(8))
print(check_even(15))


def find_larger(a, b):
    """Return the larger of two numbers."""
    if a > b:
        return a
    return b


result = find_larger(10, 20)
print("Larger number =", result)
