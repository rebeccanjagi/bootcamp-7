class Person:
	people_count = 0 #class variable. Accessed by classname.variable or object.variable
	def __init__(self, name, age):
		self.name = name #instance variable. Accessed by object.variable and NOt by classname.variable
		self.age = age
		Person.people_count += 1

	def __repr__(self):
		return "{}, {}".format(self.name,self.age)
	
	def say_hello(self):
		return "Hello, i am {} and {} years old".format(self.name, self.age)



p = Person('Becks',2)
p2 = Person('Lorna',30)
p2 = Person('Lot', 20)

print p.say_hello()

a=[('Jane',23), ('Joe',56), ('Lot',26), ('Simon',44), ('Gog',16), ('Ken',6)]
b=[]

for name, age in a:
	person =Person(name, age)
	b.append(person)
print b

for tuple_x in b:
	for o,p in tuple_x:
		print "{} said Hello!".format(o)
