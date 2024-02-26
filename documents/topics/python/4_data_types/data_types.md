# Data types 

Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, data types are classes and variables are instances (objects) of these classes. 

The following are the standard or built-in data types in Python:

* Numeric
* Sequence Type
* Boolean
* Set
* Dictionary
* Binary Types

 ![Data Types](../../../images/python/Python-data-structure.jpg)

 ## What is Python type()  Function?
To define the values ​​of various data types and check their data types we use the type() function. Consider the following examples.

This code assigns variable ‘x’ different values of various data types in Python. It covers string, integer, float, complex, list, tuple, range, dictionary, set, frozenset, boolean, bytes, bytearray, memoryview, and the special value ‘None’ successively. Each assignment replaces the previous value, making ‘x’ take on the data type and value of the most recent assignment.

```
x = "Hello World"
x = 50
x = 60.5
x = 3j
x = ["geeks", "for", "geeks"] 
x = ("geeks", "for", "geeks") 
x = range(10) 
x = {"name": "Suraj", "age": 24} 
x = {"geeks", "for", "geeks"} 
x = frozenset({"geeks", "for", "geeks"}) 
x = True
x = b"Geeks"
x = bytearray(4) 
x = memoryview(bytes(6)) 
x = None

```

