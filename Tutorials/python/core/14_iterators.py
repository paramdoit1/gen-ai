# Iterator is an object that can be iterated upon, meaning that we can traverse through all the values.
# An iterator is an object which implements the iterator protocol, which consists of the methods __iter__() and __next__()

x = ["apple", "orange", "banana"]

myiterator = iter(x)
print(myiterator.__next__())
print(myiterator.__next__())
print(myiterator.__next__())

'''
apple
orange
banana
'''

x1 = "apple"
myiter = iter(x1)

print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())
print(myiter.__next__())

'''
a
p
p
l
e
'''

x2 = ("apple", "orange", "banana")

for fruit in x2:
    print(fruit)

'''
apple
orange
banana
'''

