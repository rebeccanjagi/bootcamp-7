# -*- coding: utf-8 -*-
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
	
	list_version = input.split() #convert a string into a list
	length_of_input = len(list_version)
	result = {}

	for word in list_version:
		count = 0
		for word_2 in list_version:
			if word == word_2:
				count += 1
		result[word] = count
	return result

