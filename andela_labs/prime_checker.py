class PrimeChecker(object):
	'''
	Create a class PrimeChecker(number), that takes in a string argument. 
	When the instance of the class is called with .is_prime() it should return true 
	if number is a prime number and false if it isn't.

	'''

	def __init__(self, item1=""):
	 	self.item1 = item1

	def is_prime(self):

		if self.item1 <> '':
			x = int(self.item1)
			if x < 2:
				return True
			else:
				for i in range(2,x):
					if x % i == 0:
						return False
			return True
		else:
			return False