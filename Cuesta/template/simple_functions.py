import numpy as np

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

def test_isPrime():

    assert isPrime(3) == True
    assert isPrime(5) == True
    assert isPrime(12) == False

def isPrime(value):


    for i in range(2, int(np.sqrt(value))+ 1):

        if (value % i) == 0:
            return False 
        else:
            return True 


    return True
    


if __name__ == "__main__":

    print(isPrime(5))
