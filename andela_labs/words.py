def words(input):
	'''
	A function that counts the occurencies of words in a string 
	input : olly olly in come free" and outputs
	output:
		olly: 2
		in: 1
		come: 1
		free: 1

	'''

	list_version = input.split()
	result = {}

	for word in list_version:
		count = 0
		for word_2 in list_version:
			if word == word_2:
				count += 1
		try:
			word = int(word)
		except Exception, e:
			word = word
			
		result[word] = count
	return result


