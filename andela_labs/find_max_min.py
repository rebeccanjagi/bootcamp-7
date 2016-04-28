def find_max_min(A):
	'''
	Pass a list of integers. return the max and min value in an array 
	'''

	list_array = []
	if len(A) > 0:
		max_value = A[0]
		min_value = A[0]

		for item in A:
			if item > max_value:
				max_value = item
			if item < min_value:
				min_value = item
		if min_value == max_value:
			list_array.append(len(A))
		else:
			list_array.append(min_value)
			list_array.append(max_value)
		return  list_array
	else:
		return "List is empty"



