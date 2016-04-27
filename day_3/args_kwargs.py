def helloA(name, age):

	print "I am {} person and am {} old".format(name,age)

people = [("Jane", 23), ("Joe", 25), ("Brian",60), ("Betty",45)]





def super_sum(*args):
	'''
	Takes in variable number of items,
	and returns the sum.
	e.g super_sum(10,20) = 30
		super_sum(10, 20, 40) = 70

	
	total = 0
	for i in args:
		total += i
	return total
'''
#
#print super_sum(10, 40, 60)

#a = 10, 40, 60
#print super_sum(*a)

def hello_again(**kwargs):
	print "I am {}, and I am {}".format(kwargs['name'],kwargs['age'])

hello_again(name='becks', age=23)

joe ={'name':'joe', 'age':25}
hello_again(**joe)
hello_again(name='joe', age=23)

