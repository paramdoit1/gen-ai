# Python String
## Introduction:
A String is a data structure in Python that represents a sequence of characters. It is an immutable data type, meaning that once you have created a string, you cannot change it. Strings are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.

## What is a String in Python?
Python does not have a character data type, a single character is simply a string with a length of 1.

"Geeksforgeeks" or 'Geeksforgeeks' or "a"

## Creating a String in Python
Strings in Python can be created using single quotes or double quotes or even triple quotes. Let us see how we can define a string in Python.

`Example:`

In this example, we will demonstrate different ways to create a Python String. We will create a string using single quotes (‘ ‘), double quotes (” “), and triple double quotes (“”” “””). The triple quotes can be used to declare multiline strings in Python.

```
# Python Program for 
# Creation of String 

# Creating a String 
# with single Quotes 
String1 = 'Welcome to the Geeks World'
print("String with the use of Single Quotes: ") 
print(String1) 

# Creating a String 
# with double Quotes 
String1 = "I'm a Geek"
print("\nString with the use of Double Quotes: ") 
print(String1) 

# Creating a String 
# with triple Quotes 
String1 = '''I'm a Geek and I live in a world of "Geeks"'''
print("\nString with the use of Triple Quotes: ") 
print(String1) 

# Creating String with triple 
# Quotes allows multiple lines 
String1 = '''Geeks 
			For 
			Life'''
print("\nCreating a multiline String: ") 
print(String1) 

```

```
Output: 

String with the use of Single Quotes: 
Welcome to the Geeks World
String with the use of Double Quotes: 
I'm a Geek
String with the use of Triple Quotes: 
I'm a Geek and I live in a world of "Geeks"
Creating a multiline String: 
Geeks
            For
            Life
```
## Accessing characters in Python String
In Python, individual characters of a String can be accessed by using the method of Indexing. Indexing allows negative address references to access characters from the back of the String, e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 

While accessing an index out of the range will cause an IndexError. Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.

 ![String Indexing](../../../images/python/string_indexing.jpg)

 Example:

In this example, we will define a string in Python and access its characters using positive and negative indexing. The 0th element will be the first character of the string whereas the -1th element is the last character of the string.

```
# Python Program to Access 
# characters of String 

String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 

# Printing First character 
print("\nFirst character of String is: ") 
print(String1[0]) 

# Printing Last character 
print("\nLast character of String is: ") 
print(String1[-1]) 

```

```
Output:
Output: 


Initial String: 
GeeksForGeeks
First character of String is: 
G
Last cha racter of String is: 
s
```

## String Slicing
In Python, the String Slicing method is used to access a range of characters in the String. Slicing in a String is done by using a Slicing operator, i.e., a colon (:).  One thing to keep in mind while using this method is that the string returned after slicing includes the character at the start index but not the character at the last index.

`Example:`

In this example, we will use the string-slicing method to extract a substring of the original string. The [3:12] indicates that the string slicing will start from the 3rd index of the string to the 12th index, (12th character not including). We can also use negative indexing in string slicing.

```
# Python Program to 
# demonstrate String slicing 

# Creating a String 
String1 = "GeeksForGeeks"
print("Initial String: ") 
print(String1) 

# Printing 3rd to 12th character 
print("\nSlicing characters from 3-12: ") 
print(String1[3:12]) 

# Printing characters between 
# 3rd and 2nd last character 
print("\nSlicing characters between " +
	"3rd and 2nd last character: ") 
print(String1[3:-2]) 
```
```
Output: 

Initial String: 
GeeksForGeeks
Slicing characters from 3-12: 
ksForGeek
Slicing characters between 3rd and 2nd last character: 
ksForGee
```

## Reversing a Python String
By accessing characters from a string, we can also reverse strings in Python. We can Reverse a string by using String slicing method.

`Example:`

In this example, we will reverse a string by accessing the index. We did not specify the first two parts of the slice indicating that we are considering the whole string, from the start index to the last index.

```
#Program to reverse a string 
gfg = "geeksforgeeks"
print(gfg[::-1])

Output:

skeegrofskeeg

```

Example:

We can also reverse a string by using built-in join and reversed functions, and passing the string as the parameter to the reversed() function.

   
```
# Program to reverse a string 

gfg = "geeksforgeeks"

# Reverse the string using reversed and join function 
gfg = "".join(reversed(gfg)) 

print(gfg) 

Output:

skeegrofskeeg
```

## Deleting/Updating from a String
In Python, the Updation or deletion of characters from a String is not allowed. This will cause an error because item assignment or item deletion from a String is not supported. Although deletion of the entire String is possible with the use of a built-in del keyword. This is because Strings are immutable, hence elements of a String cannot be changed once assigned. Only new strings can be reassigned to the same name. 

### Updating a character
A character of a string can be updated in Python by first converting the string into a Python List and then updating the element in the list. As lists are mutable in nature, we can update the character and then convert the list back into the String.

Another method is using the string slicing method. Slice the string before the character you want to update, then add the new character and finally add the other part of the string again by string slicing.

`Example:`

In this example, we are using both the list and the string slicing method to update a character. We converted the String1 to a list, changes its value at a particular element, and then converted it back to a string using the Python string join() method.

In the string-slicing method, we sliced the string up to the character we want to update, concatenated the new character, and finally concatenate the remaining part of the string.

```
# Python Program to Update 
# character of a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a character of the String 
## As python strings are immutable, they don't support item updation directly 
### there are following two ways 
#1 
list1 = list(String1) 
list1[2] = 'p'
String2 = ''.join(list1) 
print("\nUpdating character at 2nd Index: ") 
print(String2) 

#2 
String3 = String1[0:2] + 'p' + String1[3:] 
print(String3) 

#Output: 

Initial String: 
Hello, I'm a Geek
Updating character at 2nd Index: 
Heplo, I'm a Geek
Heplo, I'm a Geek
```

### Updating Entire String
As Python strings are immutable in nature, we cannot update the existing string. We can only assign a completely new value to the variable with the same name.

`Example:`
In this example, we first assign a value to ‘String1’ and then updated it by assigning a completely different value to it. We simply changed its reference.

```
# Python Program to Update 
# entire String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Updating a String 
String1 = "Welcome to the Geek World"
print("\nUpdated String: ") 
print(String1) 

#Output: 

Initial String: 
Hello, I'm a Geek
Updated String: 
Welcome to the Geek World
```

### Deleting a character
Python strings are immutable, that means we cannot delete a character from it. When we try to delete thecharacter using the del keyword, it will generate an error.

```
# Python Program to delete 
# character of a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

print("Deleting character at 2nd Index:") 
del String1[2] 
print(String1)

# Output:

Initial String: 
Hello, I'm a Geek
Deleting character at 2nd Index: 
Traceback (most recent call last):
  File "e:\GFG\Python codes\Codes\demo.py", line 9, in <module>
    del String1[2]
TypeError: 'str' object doesn't support item deletion

```

But using slicing we can remove the character from the original string and store the result in a new string.

Example:

In this example, we will first slice the string up to the character that we want to delete and then concatenate the remaining string next from the deleted character.

```
# Python Program to Delete 
# characters from a String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Deleting a character 
# of the String 
String2 = String1[0:2] + String1[3:] 
print("\nDeleting character at 2nd Index: ") 
print(String2) 

# Output: 

Initial String: 
Hello, I'm a Geek
Deleting character at 2nd Index: 
Helo, I'm a Geek

```

### Deleting Entire String:
Deletion of the entire string is possible with the use of del keyword. Further, if we try to print the string, this will produce an error because the String is deleted and is unavailable to be printed.  

```
# Python Program to Delete 
# entire String 

String1 = "Hello, I'm a Geek"
print("Initial String: ") 
print(String1) 

# Deleting a String 
# with the use of del 
del String1 
print("\nDeleting entire String: ") 
print(String1) 
# 
Error: 

Traceback (most recent call last): 
File "/home/e4b8f2170f140da99d2fe57d9d8c6a94.py", line 12, in 
print(String1) 
NameError: name 'String1' is not defined 
```

## Escape Sequencing in Python
While printing Strings with single and double quotes in it causes SyntaxError because String already contains Single and Double Quotes and hence cannot be printed with the use of either of these. Hence, to print such a String either Triple Quotes are used or Escape sequences are used to print Strings. 

Escape sequences start with a backslash and can be interpreted differently. If single quotes are used to represent a string, then all the single quotes present in the string must be escaped and the same is done for Double Quotes. 
`Example:`
```
# Python Program for 
# Escape Sequencing 
# of String 

# Initial String 
String1 = '''I'm a "Geek"'''
print("Initial String with use of Triple Quotes: ") 
print(String1) 

# Escaping Single Quote 
String1 = 'I\'m a "Geek"'
print("\nEscaping Single Quote: ") 
print(String1) 

# Escaping Double Quotes 
String1 = "I'm a \"Geek\""
print("\nEscaping Double Quotes: ") 
print(String1) 

# Printing Paths with the 
# use of Escape Sequences 
String1 = "C:\\Python\\Geeks\\"
print("\nEscaping Backslashes: ") 
print(String1) 

# Printing Paths with the 
# use of Tab 
String1 = "Hi\tGeeks"
print("\nTab: ") 
print(String1) 

# Printing Paths with the 
# use of New Line 
String1 = "Python\nGeeks"
print("\nNew Line: ") 
print(String1) 
```

```
Output:

Initial String with use of Triple Quotes: 
I'm a "Geek"
Escaping Single Quote: 
I'm a "Geek"
Escaping Double Quotes: 
I'm a "Geek"
Escaping Backslashes: 
C:\Python\Geeks\
Tab: 
Hi    Geeks
New Line: 
Python
Geeks
```

`Example:`

To ignore the escape sequences in a String, r or R is used, this implies that the string is a raw string and escape sequences inside it are to be ignored.

```
# Printing hello in octal 
String1 = "\110\145\154\154\157"
print("\nPrinting in Octal with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ") 
print(String1) 

# Printing Geeks in HEX 
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ") 
print(String1) 

# Using raw String to 
# ignore Escape Sequences 
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ") 
print(String1) 

Output:

Printing in Octal with the use of Escape Sequences: 
Hello
Printing Raw String in Octal Format: 
This is \110\145\154\154\157
Printing in HEX with the use of Escape Sequences: 
This is Geeks in HEX
Printing Raw String in HEX Format: 
This is \x47\x65\x65\x6b\x73 in \x48\x45\x58

```

## Formatting of Strings
Strings in Python can be formatted with the use of format() method which is a very versatile and powerful tool for formatting Strings. Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.

`Example 1:`

In this example, we will declare a string which contains the curly braces {} that acts as a placeholders and provide them values to see how string declaration position matters.

```
# Python Program for 
# Formatting of Strings 

# Default order 
String1 = "{} {} {}".format('Geeks', 'For', 'Life') 
print("Print String in default order: ") 
print(String1) 

# Positional Formatting 
String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life') 
print("\nPrint String in Positional order: ") 
print(String1) 

# Keyword Formatting 
String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life') 
print("\nPrint String in order of Keywords: ") 
print(String1) 
# Output: 

Print String in default order: 
Geeks For Life
Print String in Positional order: 
For Geeks Life
Print String in order of Keywords: 
Life For Geeks

```

`Example 2:`

Integers such as Binary, hexadecimal, etc., and floats can be rounded or displayed in the exponent form with the use of format specifiers. 

```
# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 

# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 

# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 

# 
# Formatting of Integers 
String1 = "{0:b}".format(16) 
print("\nBinary representation of 16 is ") 
print(String1) 
  
# Formatting of Floats 
String1 = "{0:e}".format(165.6458) 
print("\nExponent representation of 165.6458 is ") 
print(String1) 
  
# Rounding off Integers 
String1 = "{0:.2f}".format(1/6) 
print("\none-sixth is : ") 
print(String1) 

#Output: 

Binary representation of 16 is 
10000
Exponent representation of 165.6458 is 
1.656458e+02
one-sixth is : 
0.17
```

[Back](./README.md)
