

#function to calculate a Fibonacci sequence upto a given number 
def fibonacci(max):
#define the first two numbers of the sequence
    values = [0, 1]
#create the fibonacci sequence by adding all previous numbers to create the next number in the sequence 
    while values[-2] + values[-1] < max:
        values.append(values[-2] + values[-1])
    return values


#function to calculate a factorial of a given number 
def factorial(value):
#value of 0!=1
    if value == 0:
        return 1
#factorial n = n*(n-1)*(n-2)*....*1
    else:
        return value * factorial(value - 1)

#function to check if a number is prime
def is_prime(value):
#remove 1 and 2 as they are godly primes  
	if value > 2.:
		for i in range(2,value):
#check if it is divisible by any number less than this number		
			if value % i == 0.:
				return False
			else:
				return True
	else:
		print('All hail no. 1, the primest of all and also 2')
