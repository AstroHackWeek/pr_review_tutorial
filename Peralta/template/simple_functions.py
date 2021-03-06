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
    assert type(value) is int

    if value > 1:
        # Initialise the result as True
        result = True

        # Try to find a integer which divides the input value:
        # If we find one, the result will be changed to False
        
        max_test_int = math.floor(math.sqrt(value))

        for i in range(2, max_test_int + 1):
            if value % i == 0:
                result = False
                break
    else:
        result = False

    return result

