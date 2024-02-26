# String Methods:
Python string is a sequence of Unicode characters that is enclosed in quotation marks. In this article, we will discuss the in-built string functions i.e. the functions provided by Python to operate on strings.

## Case Changing of Strings
The below Python functions are used to change the case of the strings. Let’s look at some Python string methods with examples:

lower(): Converts all uppercase characters in a string into lowercase
upper(): Converts all lowercase characters in a string into uppercase
title(): Convert string to title case
swapcase(): Swap the cases of all characters in a string
capitalize(): Convert the first character of a string to uppercase

### Example: Changing the case of Python Strings

```
# Python3 program to show the 
# working of upper() function 
text = 'geeKs For geEkS'

# upper() function to convert 
# string to upper case 
print("\nConverted String:") 
print(text.upper()) 

# lower() function to convert 
# string to lower case 
print("\nConverted String:") 
print(text.lower()) 

# converts the first character to 
# upper case and rest to lower case 
print("\nConverted String:") 
print(text.title()) 

#swaps the case of all characters in the string 
# upper case character to lowercase and viceversa 
print("\nConverted String:") 
print(text.swapcase()) 

# convert the first character of a string to uppercase 
print("\nConverted String:") 
print(text.capitalize()) 

# original string never changes 
print("\nOriginal String") 
print(text)

```

```
Output
Converted String:
GEEKS FOR GEEKS

Converted String:
geeks for geeks

Converted String:
Geeks For Geeks

Converted String:
GEEkS fOR GEeKs

Original String
geeKs For geEkS
Time complexity: O(n) where n is the length of the string ‘text’
Auxiliary space: O(1)


```

##   List of Python String Methods
Here is the list of in-built Python string methods, that you can use to perform actions on string:

Function Name 	Description
capitalize()	Converts the first character of the string to a capital (uppercase) letter
casefold()	Implements caseless string matching
center()	Pad the string with the specified character.
count()	Returns the number of occurrences of a substring in the string.
encode()	Encodes strings with the specified encoded scheme
endswith()	Returns “True” if a string ends with the given suffix
expandtabs()	Specifies the amount of space to be substituted with the “\t” symbol in the string
find()	Returns the lowest index of the substring if it is found
format()	Formats the string for printing it to console
format_map()	Formats specified values in a string using a dictionary
index()	Returns the position of the first occurrence of a substring in a string
isalnum()	Checks whether all the characters in a given string is alphanumeric or not
isalpha()	Returns “True” if all characters in the string are alphabets
isdecimal()	Returns true if all characters in a string are decimal
isdigit()	Returns “True” if all characters in the string are digits
isidentifier()	Check whether a string is a valid identifier or not
islower()	Checks if all characters in the string are lowercase
isnumeric()	Returns “True” if all characters in the string are numeric characters
isprintable()	Returns “True” if all characters in the string are printable or the string is empty
isspace()	Returns “True” if all characters in the string are whitespace characters
istitle()	Returns “True” if the string is a title cased string
isupper()	Checks if all characters in the string are uppercase
join()	Returns a concatenated String
ljust()	Left aligns the string according to the width specified
lower()	Converts all uppercase characters in a string into lowercase
lstrip()	Returns the string with leading characters removed
maketrans()	 Returns a translation table
partition()	Splits the string at the first occurrence of the separator 
replace()	Replaces all occurrences of a substring with another substring
rfind()	Returns the highest index of the substring
rindex()	Returns the highest index of the substring inside the string
rjust()	Right aligns the string according to the width specified
rpartition()	Split the given string into three parts
rsplit()	Split the string from the right by the specified separator
rstrip()	Removes trailing characters
splitlines()	Split the lines at line boundaries
startswith()	Returns “True” if a string starts with the given prefix
strip()	Returns the string with both leading and trailing characters
swapcase()	Converts all uppercase characters to lowercase and vice versa
title()	Convert string to title case
translate()	Modify string according to given translation mappings
upper()	Converts all lowercase characters in a string into uppercase
zfill()	Returns a copy of the string with ‘0’ characters padded to the left side of the string
