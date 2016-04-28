def data_type(A):
	'''
	A function that takes one input and outputs:
		-For strings, return its length.
		-For None return string 'no value'
		-For booleans return the boolean
		-For integers return a string showing how it compares to hundred 
		e.g. For 67 return 'less than 100' for 4034 return 'more than 100' or equal to 100 as the case may be
		-For lists return the 3rd item, or None if it doesn't exist

	'''
	try:
		if type(A) == str:
			return len(A)
		elif A == None:
			return 'no value'
		elif type(A) == bool:
			return A
		elif type(A) == int:
			if A > 100:
				return "more than 100"
			elif A < 100:
				return "less than 100"
			elif A == 100:
				return "equal to 100"
		elif type(A) == list:
			if len(A) >= 3:
				counter = 0
				for t in A:
					counter += 1
					if counter == 3:
						return t
			else:
				return None
		else:
			return "invalid argument"
	except Exception, e:
		return "invalid argument"