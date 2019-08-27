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

def is_prime(number):
    if not isinstance(number, int):
        return False

    if number <= 2:
        return False
    
    divider = 2
    prime = True
    
    while divider < number:
        if float(number)%divider == 0.0:
            # If divisible by divider without remainder, it is not a prime
            prime = False
            break
        else:
            # Else, check next divider
            divider += 1
    
    return prime