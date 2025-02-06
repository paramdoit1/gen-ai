# Python Membership and Identity Operators

Python offers two membership operators to check or validate the membership of a value. It tests for membership in a sequence, such as strings, lists, or tuples. 

## in operator:
The ‘in’ operator is used to check if a character/ substring/ element exists in a sequence or not. Evaluate to True if it finds the specified element in a sequence otherwise False. For example,

```
'G' in 'GeeksforGeeks'   # Checking 'G' in String
True
'g' in 'GeeksforGeeks'   #Checking 'g' in string since Python is case-sensitive,returns False
False
'Geeks' in ['Geeks', 'For','Geeks']   #Checking 'Geeks' in list of strings
True
10 in [10000,1000,100,10]        #Checking 10 in list of integers
True
dict1={1:'Geeks',2:'For',3:'Geeks'}     # Checking 3 in keys of dictionary
3 in dict1
True
```

```
# Python program to illustrate
# Finding common member in list
# using 'in' operator
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
	if item in list2:
		print("overlapping")
	else:
		print("not overlapping")

```

## ‘not in’ operator
Evaluates to true if it does not finds a variable in the specified sequence and false otherwise.

```
# Python program to illustrate
# not 'in' operator
x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
	print("x is NOT present in given list")
else:
	print("x is present in given list")

if (y in list):
	print("y is present in given list")
else:
	print("y is NOT present in given list")

Output
x is NOT present in given list
y is present in given list
```

## Identity operators
Identity operators are used to compare the objects if both the objects are actually of the same data type and share the same memory location.
There are different identity operators such as 

### ‘is’ operator 
Evaluates to True if the variables on either side of the operator point to the same object and false otherwise.

```
# Python program to illustrate the use
# of 'is' identity operator
x = 5
y = 5
print(x is y)
id(x)
id(y)

# Output
True

```

## ‘is not’ operator:

Evaluates True if both variables are not the same object.

```
x = ["Geeks", "for", "Geeks"]
y = ["Geeks", "for", "Geeks"]
z = x

# Returns False because z is the same object as x
print(x is not z)

# Returns True because x is not the same object as y,
# even if they have the same content
print(x is not y)

# To demonstrate the difference between "is not" and "!=":
# This comparison returns False because x is equal to y
print(x != y)

# Output
False
True
False
```

[Back](./README.md)


