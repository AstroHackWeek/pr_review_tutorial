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


def isprime(n):
    if n < 4:
        return True
    if n%2==0 or n%3==0:
        return False
    i = 5
    while i**2<=n:
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True 
