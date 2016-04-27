def data_type(x):
	'''
	Takes in an argument,x:
		- For an integer, return x ** 2
		- For a float, return x /2
		- For a string, returns "Hello" + x
		- For a boolean, return "boolean"
		- For a long, return square root(x)
	'''
	
	try:

		if type(x) == int: #Checks if x is an integer
			return x ** 2
		elif type(x) == float: #Checks if x is a float
			return x / 2
		elif type(x) == str: #Checks if x is a string
			return "Hello {}".format(x)
		elif type(x) == bool: #Checks if x is a boolean
			return "boolean"
		elif type(x) == long: #Checks if x is long
			return "long"
		else:
			return "Invalid data type" 

	except Exception, e:
		return "Invalid data type" #handles any exception
	
