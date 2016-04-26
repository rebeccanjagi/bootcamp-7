def sum_digits(A):
	'''
	Takes in a list A, and returns the sum of all
	digits in the list. E.g [10,30,45] should return 
	1 + 0 + 3 + 0 + 4 + 5

	'''
	int_value = 0

	for list_value in A:

		str_value = str(list_value)

		for char_value in str_value:
			int_value += int(char_value)

	print int_value

sum_digits([10,30,45])

