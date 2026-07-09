import math


# Decorator to check if the number is positive
def validate_positive(func):
    def wrapper(n):
        if n < 0:
            raise ValueError("Negative numbers are not allowed!")
        return func(n)
    return wrapper


# Apply the decorator
@validate_positive
def square_root(n):
    return math.sqrt(n)


# Test the function
print(square_root(25))

# Uncomment the line below to test the error
# print(square_root(-9))