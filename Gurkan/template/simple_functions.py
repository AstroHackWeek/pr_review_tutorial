from math import sqrt, ceil, floor
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
    '''
    A function to check whether the argument is a prime number.

    This function uses the sieve of Eratoshenes to check whether its
    input is a prime number.
    It expects an integer, but it can be represented as a float, e.g.,
    7.0 is OK, but 7.1 is not.

    Parameters
    ----------
    n : integer
        The input.
    Returns
    -------
    Boolean
        True if the input is a prime, False otherwise.
    '''
    if floor(n) != n:
        raise OSError('input to is_prime() should be an integer!')
##    if not(isinstance(n, numbers.Integral)):
##        return False
    if (n <= 1):
        return False
    for i in range(2, ceil(sqrt(n))+1):
        if (n % i == 0):
            return False
    return True
