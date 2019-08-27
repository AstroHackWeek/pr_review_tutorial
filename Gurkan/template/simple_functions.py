from math import sqrt, ceil
import numbers


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


def is_prime(n):
    ''' This function checks whether the arguments is a prime number.
    It expects an integer, so an input like 7.0 is going to return
    False.
    '''
    if not(isinstance(n, numbers.Integral)):
        return False
    if (n <= 1):
        return False
    for i in range(2, ceil(sqrt(n))+1):
        if (n % i == 0):
            return False
    return True
