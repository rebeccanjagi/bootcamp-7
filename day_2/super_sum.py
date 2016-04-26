def super_sum(A):
	''' 
	Takes a list A, and :
			-Halves every even number
			-Doubles every odd number
		And returns the sum of all.

	'''
	result = 0

	for list_value in A:

		if list_value % 2 == 0:
			result += list_value / 2
		else:
			result += list_value * 2

	return result
