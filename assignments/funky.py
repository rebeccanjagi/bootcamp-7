def Funky(a, b):
	'''
	Funky takes in a and b. Funky should perform an addition operation to a and b

	'''
	try:
				
		if type(a) and type(b) == str:
			#concatenates strings
			return a+b

		elif type(a) and type(b) == int or type(a) and type(b) == float:
			#adds integers or floats
			return a+b

		elif type(a) and type(b) == list:
			#adds the values of a list
			return a+b

		elif type(a) and type(b) == dict:
			#adds the values of a dictionary
			list_a = a.values()
			list_b = b.values()
			return list_a + list_b
			
		else:
			return "Something is wrong..."

	except Exception, e:
		return "Operand mismatch"





