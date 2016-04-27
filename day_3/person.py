#Super Class
class Person(object):

	people_count = 0 #class variable. Accessed by classname.variable or object.variable

	def __init__(self, name, age):
		self.name = name #instance variable. Accessed by object.variable and NOt by classname.variable
		self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "<object: {}, {}>".format(self.name,self.age)
	
	def say_hello(self):
		return "Hello, i am {}. I am {} years old".format(self.name, self.age)

