a = [10, 40, -9, 45, 60, 89]
print a

#print each value in a on a seperate line

for i in a:
    print i

#print contents of a in reverse - example 1

len_a = len(a)

while len_a > 0:
	print a[len_a - 1]
	len_a -= 1


#print contents of a in reverse - example 2
for index in range(len(a) - 1, -1, -1):
	print a[index]



#A function that gives its output as
#   x:2, y:4
#   x:5, y:10
b=[(2,4), (5,10), (6,20), (50,50)]

def list_tuple(A):

	for latitude, longitude in A:
		print "x:{}, y:{}".format(latitude,longitude)

list_tuple(b)

