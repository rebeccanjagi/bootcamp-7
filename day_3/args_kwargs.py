# unpacking
def hello(name, age, class_=''):
    '''
    A function that tests the format function and outputs
    '''
    if class_ != '':
        return "I am {}, {} y/o, and {} class".format(name, age, class_)
    return "I am {}, and I'm {}".format(name, age)


people = [
            ("Jane", 23, 'High'),
            ("Joe", 25, 'Low'),
            ("Brian", 60),
            ("Betty", 45)
         ]


# unpacking

for person in people:
    print hello(*person)


def super_sum(a, b, *args): #args is not a reserved word. takes in a tuple
    '''
    Takes in variable number of items,
    and returns the sum.
    e.g. super_sum(10, 20) = 30
        super_sum(10, 20, 40) = 70
        super_sum(1, 4, 5, 6, 7) = 23
    '''
    total = 0
    for i in args:
        total += i

    return total + a + b

print super_sum(10, 20)
print super_sum(1, 4, 5, 7)
a = [10, 40, 60]
print super_sum(*a)
print super_sum(10, 20)

def hello_again(**kwargs): #kwargs is not a reserved word. Takes in a dictionary
    return "I am {}, and I'm {}".format(kwargs['name'], kwargs['age'])


print hello_again(name='Joe', age=20)
print hello_again(age=20, name='Jane')

joe = {'name': 'Joe', 'age': 98}

print hello_again(**joe)
print hello_again(name='Joe', age=98)

other_people = [
        {'name': 'Joe', 'age': 98},
        {'name': 'Jane', 'age': 60},
        {'name': 'Trump', 'age': 23}
    ]

for person in other_people:
    hello_again(**person)
