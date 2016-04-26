def sum_digits(A):
	'''
	Takes in a list A, and returns the sum of all
	digits in the list. E.g [10,30,45] should return 
	1 + 0 + 3 + 0 + 4 + 5

	'''
	int_value = 0

	#loops through the values of the list
	for list_value in A:
		#converts each list value into a string to enable iteration
		str_value = str(list_value)
		#iterates through the characters of the string
		for char_value in str_value:
			#converts the characters into integer to enable addition
			int_value += int(char_value)

	return int_value


