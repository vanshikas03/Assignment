def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("Sum =", result)


def check_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(check_even(8))
print(check_even(15))


def find_larger(a, b):
    if a > b:
        return a
    else:
        return b


result = find_larger(10, 20)
print("Larger number =", result)
