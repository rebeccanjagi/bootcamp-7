def reverse_string(string):
	'''
	A function, reverse_string(string), that returns the reverse of the string provided. 
	If the reverse of the string is the same as the original string, 
	as in the case of palindromes, return true instead.

	'''


	if string is not "":
		for b in string:
			rev_string = b+rev_string
		if rev_string == string:
			return True
		return rev_string
	else:
		return None
