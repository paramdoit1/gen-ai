'''
Text Type: str
Numeric Type:  int, float, complex
sequence types: list, tuple, range
Mapping type: dict
Set Types: set, frozenset
'''

#Setting the data types:

#String
x_str_1 = "hello world"
print(x_str_1)
#hello world

#int
x_str_2 = 10
print(x_str_2)
#10

#Boolean
#Boolean represent one of two values: True or False
#We can evaluate any expression in python and get one of two answers, True or False

print(10>9)
#True

#bool() function allows you to evaluate any value, and give True or False in return
print(bool("world"))
#True

print(bool(10))
#True

print(bool(0))
#False

#Method with Boolean
def myFunction():
    return True

result = myFunction()
print(result)
#True

if myFunction:
    print("YES")
else:
    print("NO")

#YES

#Float
x_float_3 = 20.0
print(x_float_3)
#20.0

print(type(x_float_3))
#<class 'float'>

#Complex
#real and imaginary roots contribution are called complex numbers

x_complex_4 = 4+3j
#4i+3j or 4 +3j
print(x_complex_4)
#(4+3j)

#List
#Lists are used to store multiple items in a single variable.
# The lists are changeable, meaning that we can change, add, and remove items in a list after it has been created.
#To determine how many items  a list has, use the len() function
#it is also possible to use the list() constructor when creating a new list

x_list_5= ['apple', 'orange', 'banana']
print(x_list_5)
#['apple', 'orange', 'banana']

#Tuples
#Tuples are used to store multiple items in a single variable.
# A tuple is  a collection which is ordered and not changeable.

x_tuple_6 = ('apple', 'orange', 'banana')
print(x_tuple_6)

#('apple', 'orange', 'banana')

# Range
# returns a sequence of numbers, starting from 0 by default
# and increments of 1(by default), and stops before specified number
#The stop value for last number is -1

#Syntax
#range(stop)
#range(start, stop)
#range(start, stop, step)
x_range_7 = range(6)
print(x_range_7)
#range(0, 6)

for i in x_range_7:
    print(i)

'''
0
1
2
3
4
5
'''


x_range_8 = range(1, 7, 2)
print(x_range_8)
#range(1, 7, 2)

for i in x_range_8:
    print(i)

'''
1
3
5
'''

#Set
# Sets are used to store multiple items in a single variable
# Sets cannot have two items with same value
# Set items are unordered, unchangeable, and do not allow duplicate values
# Once a set is created, we cannot change its items, but we can remove items and add new items

x_set_1 = {'apple', 'orange', 'banana', 'apple'}
print(x_set_1)

# {'apple', 'orange', 'banana'}

#Dictionary
#Dictionaries are used to store data values in key:value paris
#Dictionary items are presented in key:value pairs, and can be referred by using key name
# A dictionary is a collection which is ordered, changeable and do not allow duplicate keys

x_dict_1 = {
    'name': 'apple',
    'type' : 'fruit',
    'color': 'red'
}

print('dictionary item: ', x_dict_1['name'])
#dictionary item:  apple

