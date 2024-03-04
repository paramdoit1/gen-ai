# Python string length 
The string len() function returns the length of the string. In this article, we will see how to find the length of a string using the string len() method.

```
string = "Geeksforgeeks"
print(len(string))

# Output
13

```

## What is the String len() Function?
The string len() function is a built-in function in Python that is used to find the length of the string. You can know the number of characters in a string using this function.

It is a very important string function, and it is very easy to use.

## How to Use String len() Function?
You can easily use the String len() function, just pass the string as the parameter in the function. Let’s look at an example to understand how to find the length of the string in Python.

More Examples of String len() Function
The len() method is used to find the length of an object in Python. By using len(), we can find the length of strings and lists. In this example, we are finding the length of a string.

### Example 1: Len() function with tuples and string    

```

# Python program to demonstrate the use of
# len() method 

# with tuple
tup = (1,2,3)
print(len(tup))

# with list
l = [1,2,3,4]
print(len(l))

# Output
3
4

```

###  Example 2: Python len() TypeError
In this example, we are using len() with a boolean value and find TypeError as a result.

```
print(len(True))

# Output

TypeError: object of type 'bool' has no len()
```

### Example 3: Python len() with dictionaries and sets
In this example, we are using Python len() with dictionaries and sets to find the length of dictionary and set.

```

# Python program to demonstrate the use of
# len() method 

dic = {'a':1, 'b': 2}
print(len(dic))

s = { 1, 2, 3, 4}
print(len(s))

# Output
2
4
```

### Example 4: Python len() with range()
In this example, we are using the len() function to find the length of the range() function.

```
l=range(1,10)
print(len(l))
# Output
9
```

[Back](./README.md)
