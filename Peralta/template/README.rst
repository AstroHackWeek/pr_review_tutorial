This folder contains two Python scripts: simple\_functions.py and buggy\_function.py.

Simple functions
----------------

Factorial
~~~~~~~~~

There is a function for computing the factorial of an integer number:

    >>> from simple_functions import factorial
    >>> factorial(10)
    3628800

Fibonnacci
~~~~~~~~~~

There is a function for computing the Fibonnacci numbers lower than a given integer:

    >>> from simple_functions import fibonacci
    >>> fibonacci(100)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

Is prime?
~~~~~~~~~

There is a function for guessing whether a given integer is a prime number:

    >>> from simple_functions import is_prime
    >>> is_prime(9)
    False

Buggy function
--------------

Angle to sexigesimal
~~~~~~~~~~~~~~~~~~~~

There is a function for guessing whether a given integer is a prime number:

    >>> from buggy_function import angle_to_sexigesimal
    >>> angle_to_sexigesimal(0.5, decimals=4)
    '0:2:0.0000'

