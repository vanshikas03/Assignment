# Countdown Generator

def countdown(n):
    while n >= 0:
        yield n
        n -= 1


# Rocket Launch Countdown
for number in countdown(10):
    print(number)
