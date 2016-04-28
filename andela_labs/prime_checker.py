class PrimeChecker(object):
	'''
	Create a class PrimeChecker(number), that takes in a string argument. 
	When the instance of the class is called with .is_prime() it should return true 
	if number is a prime number and false if it isn't.

	'''

	def __init__(self, item1):
	 	self.item1 = item1

	def is_prime(self):

		if self.item1 is not '':
			x = int(self.item1)
			if x < 2:
				return True
			else:
				if x > 1:
					if x % x == 0:
						return True
		return False
		
			

p = PrimeChecker('3')
print p.is_prime()


