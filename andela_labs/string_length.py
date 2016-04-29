def string_length(A):
	'''
	This function should return the length of the string, or strings in a list
	['Fairy', 'tale'] should return [5, 4]
	'C-sharp' should return [7]
	
	'''
	result = []
	if type(A) == str:
		result.append(len(A))		
	elif type(A) == list:
		for string in A:
			result.append(len(string))

	return result


		