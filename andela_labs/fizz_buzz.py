def fizz_buzz(A):

	'''
	A function fizz_buzz that returns 'Fizz', 'Buzz', 'FizzBuzz', or the argument it receives, 
	all depending on the argument of the function, a number that is divisible by, 3, 5, or both 3 and 5, respectively.

	When the number is not divisible by 3 or 5, the number itself should be returned.

	'''
	if A % 3 == 0 and A % 5 == 0:
		return "FizzBuzz"
	else:
		if A % 3 == 0:
			return "Fizz"
		elif A % 5 == 0:
			return "Buzz"
		else:
			return A
