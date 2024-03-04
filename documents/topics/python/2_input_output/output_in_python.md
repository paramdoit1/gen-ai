# Output using print() function
Python print() function prints the message to the screen or any other standard output device. In this article, we will cover about print() function in Python as well as it’s various operations.

```
Syntax : print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

Parameters: 

value(s): Any value, and as many as you like. Will be converted to a string before printed
sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
file : (Optional) An object with a write method. Default :sys.stdout
flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False
Return Type: It returns output to the screen.

```

## How print() works in Python?
We can pass variables, strings, numbers, or other data types as one or more parameters when using the print() function. Then, these parameters are represented as strings by their respective str() functions. To create a single output string, the transformed strings are concatenated with spaces between them.

In this code, we are passing two parameters name and age to the print function.

```

name = "Alice"
age = 25

print("Hello, my name is", name, "and I am", age, "years old.")

# Output:
Hello, my name is Alice and I am 25 years old.

```

## Python String Literals

String literals in Python’s print statement are primarily used to format or design how a specific string appears when printed using the print() function.

\n: This string literal is used to add a new blank line while printing a statement.
“”: An empty quote (“”) is used to print an empty line.

`print("GeeksforGeeks \n is best for DSA Content.")`

```
Output
GeeksforGeeks 
 is best for DSA Content.
```

## Python “end” parameter in print()
The end keyword is used to specify the content that is to be printed at the end of the execution of the print() function. By default, it is set to “\n”, which leads to the change of line after the execution of print() statement.

In this example, we are using print() with end and without end parameters.

```
# This line will automatically add a new line before the
# next print statement
print ("GeeksForGeeks is the best platform for DSA content")

# This print() function ends with "**" as set in the end argument.
print ("GeeksForGeeks is the best platform for DSA content", end= "**")
print("Welcome to GFG")

```

```
Output
GeeksForGeeks is the best platform for DSA content
GeeksForGeeks is the best platform for DSA content**Welcome to GFG
```

## Print Concatenated Strings:

In this example, we are concatenating strings inside print() function in Python.

```
print('GeeksforGeeks is a Wonderful ' + 'Website.')
#GeeksforGeeks is a Wonderful Website.
```
## Output formatting
In this example, we are formatting our output to make it look more attractive by using str.format() function.

```
a,b,=10,1000
print('The value of a is {} and b is {}'.format(a,b))
The value of a is 10 and b is 1000

```

[Back](./README.md)
