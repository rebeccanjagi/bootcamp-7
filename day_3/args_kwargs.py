def hello(name, age):

	'''

	'''
	print "I am {} person and am {} old".format(name,age)

people = [("Jane", 23), ("Joe", 25), ("Brian",60), ("Betty",45)]

for name, age in a:
	print hello(name, age)

#unpacking a tuple
for person in people:
	print hello(*person)



