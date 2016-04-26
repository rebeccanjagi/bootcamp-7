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
			#concatenates the values of the lists
			return a+b

		elif type(a) and type(b) == dict:
			#adds the values of the dictionaries
			list_a = a.values()
			list_b = b.values()
			return list_a + list_b
			
		else:
			return "Something is wrong..."

	except Exception, e:
		return "Operand mismatch"





