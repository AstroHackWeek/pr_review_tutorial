def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_prime(value):
    if value % 2.0 == 0 or value % 3.0 == 0 or value % 5.0 == 0 or valye % 7.0 == 0:
        print("False")
    else:
        print("True")
