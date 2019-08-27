"""Summary
"""
from math import sqrt

def fibonacci(max):
    """Generate Fibonacci sequence up to given value
    
    Parameters
    ----------
    max : int
        Max value of sequence
    
    Returns
    -------
    list
        Fibonacci sequence
    """
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value):
    """Summary
    
    Parameters
    ----------
    value : TYPE
        Description
    
    Returns
    -------
    TYPE
        Description
    """
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)

def is_prime(value):
    """Check if value is prime
    
    Parameters
    ----------
    value : int
        Value to check for primeness
    
    Returns
    -------
    boolean
        True if prime, False otherwise
    """
    for i in range(2, int(sqrt(value)) + 1):
        if value % i == 0:
            return False

    return True
