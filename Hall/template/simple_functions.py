def fibonacci(max):
    values = [0, 1]
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


def factorial(value: int):
    """ A function that returns the factorial of the input value. The factorial
    is calculated by recusrively multiplying with each integer below the input
    value.

    Input
    ------
    value : int
        The value for which the factorial is calculated, eg: 4 would return 4!
        Must be an positive integer.

    Returns
    ------
    factorial : int
        The factorial of the input value.
    """
    if type(value) is not int:
        raise ValueError('Value must be an integer.')

    if value < 0:
        raise ValueError('Value must be a positive integer.')

    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)
