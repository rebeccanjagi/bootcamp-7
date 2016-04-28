def factorial(number):
	if type(number) == int:
		result = 1
		for i in range(number,0,-1):
			result = result * i
		print result


factorial(5)