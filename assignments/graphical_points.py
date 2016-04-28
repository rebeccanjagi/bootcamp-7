def graphical_points(points):
	'''
	A function that receives a list of tuples as input and ouputs:
	x: 10, y: 20, z 40
	x: 10, y: 6
	x: 80, y: 60

	'''
	try:
		pass
	
		for tuple_i in points:

			if type(tuple_i) == int: #check if only one value is passed because it cannot be iterated.
				return "x: {}".format(tuple_i)
			else:
			 	tuple_length = len(tuple_i) #get the tuple length

			if tuple_length == 3:
				return "x: {}, y: {}, z: {}".format(tuple_i[0],tuple_i[1],tuple_i[2])

			elif tuple_length == 2:
				return "x: {}, y: {}".format(tuple_i[0],tuple_i[1])

			elif tuple_length == 1:
				return "x: {}".format(tuple_i)

			else :
				return "Tuple values should be less than 3"

	except Exception, e:
		return "Tuple values should be less than 3"


