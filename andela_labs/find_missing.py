def find_missing(A, B):
	

	same_list = []

	if len(A) <  len(B):
		longer_list = B
		shorter_list = A
	elif len(A) >  len(B):
		longer_list = A
		shorter_list = B
	elif len(A) ==  len(B) and len(A) != 0 and len(B) != 0 :
		if A[0] == B[0]:
			return 0
	elif len(A) == 0 and len(B) == 0:
		return 0


	for value_list_1 in shorter_list:
		for value_list_2 in longer_list:
			if value_list_1== value_list_2:
				longer_list.remove(value_list_1)

	return longer_list[0]

# list1 = find_missing([1, 2], [1, 2, 5])
# list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
list1 = find_missing([1, 2], [1, 2, 5])
list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
list3 = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
print [list1, list2, list3]
# print list1
