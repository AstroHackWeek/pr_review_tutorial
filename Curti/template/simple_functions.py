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


def is_prime(a) : 

	if a >= 2 : 
		for i in range(2,a) : 
			if not (a%i) : 
				return False
	elif a ==1 : 
		return True			
	else : 
		return False		

	return True	



