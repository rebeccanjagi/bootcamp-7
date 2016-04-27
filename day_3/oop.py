from person import Person
from kenyan import Kenyan

#tests using imports from person module
p = Person('Becks',2)
p2 = Person('Lorna',30)
p2 = Person('Lot', 20)

print p.say_hello()

a=[('Jane',23), ('Joe',56), ('Lot',26), ('Simon',44), ('Gog',16), ('Ken',6)]
b=[]

for name, age in a:
	person = Person(name, age)
	b.append(person)

print b

for w in b:
	print w.say_hello()

#tests using imports from kenyan module

k = Kenyan('Jane', 20)

k.probe(True)

print "Is {} corrupt? {}".format(k.name, k.is_corrupt())

print k.say_hello()
