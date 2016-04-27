people = [
('Jack',78),
('Janet', 45),
('Lot', 63)
]



def super_sum(*args):
	return sum(args)


def hello_again(name, age):
	return "I am {}. I am {} years old".format(name,age)


def max_min(A):
	'''
	returns the max value - min value

	'''
	#return max(A) - max(B)
	max_, min_ = A[0], A[0]

	for i in A:

		if i > max_:
			max_ = i
		if i < min_:
			min_ = i

	return max_ - min_
