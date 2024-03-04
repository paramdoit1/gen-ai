# Python RegEx
## Introduction
A RegEx is a powerful tool for matching text, based on a pre-defined pattern. It can detect the presence or absence of a text by matching it with a particular pattern, and also can split a pattern into one or more sub-patterns. The Python standard library provides a re module for regular expressions. Its primary function is to offer a search, where it takes a regular expression and a string. Here, it either returns the first match or else none.

```
import re 


match = re.search(r'portal', 'GeeksforGeeks: A computer science \ 
				portal for geeks') 
print(match) 
print(match.group()) 

print('Start Index:', match.start()) 
print('End Index:', match.end()) 

#Output:
<_sre.SRE_Match object; span=(52, 58), match='portal'>
portal
Start Index: 52
End Index: 58
```
Here r character (r’portal’) stands for raw, not RegEx. The raw string is slightly different from a regular string, it won’t interpret the \ character as an escape character. This is because the regular expression engine uses \ character for its own escaping purpose.

Before starting with the Python regex module let’s see how to actually write RegEx using metacharacters or special sequences. 

## MetaCharacters:

To understand the RE analogy, MetaCharacters are useful, important, and will be used in functions of module re. Below is the list of metacharacters.

MetaCharacters	Description
\	Used to drop the special meaning of character following it
[]	Represent a character class
^	Matches the beginning
$	Matches the end
.	Matches any character except newline
|	Means OR (Matches with any of the characters separated by it.
?	Matches zero or one occurrence
*	Any number of occurrences (including 0 occurrences)
+	One or more occurrences
{}	Indicate the number of occurrences of a preceding RegEx to match.
()	Enclose a group of RegEx

The group method returns the matching string, and the start and end method provides the starting and ending string index. Apart from this, it has so many other methods, which we will discuss later.

## Why RegEx?

Let’s take a moment to understand why we should use Regular expression.

* Data Mining: Regular expression is the best tool for data mining. It efficiently identifies a text in a heap of text by checking with a pre-defined pattern. Some common scenarios are identifying an email, URL, or phone from a pile of text.
* Data Validation: Regular expression can perfectly validate data. It can include a wide array of validation processes by defining different sets of patterns. A few examples are validating phone numbers, emails, etc.

### Basic RegEx
Let’s understand some of the basic regular expressions. They are as follows:

Character Classes
Rangers
Negation
Shortcuts
Beginning and End of String
Any Character
Character Classes
Character classes allow you to match a single set of characters with a possible set of characters. You can mention a character class within the square brackets. Let’s consider an example of case sensitive words. 

```
   
import re 
  
  
print(re.findall(r'[Gg]eeks', 'GeeksforGeeks: \ 
                 A computer science portal for geeks'))

#Output:
['Geeks', 'Geeks', 'geeks']

```

### Shortcuts
Let’s discuss some of the shortcuts provided by the regular expression engine.

\w – matches a word character
\d – matches digit character
\s – matches whitespace character (space, tab, newline, etc.)
\b – matches a zero-length characte

```
import re 


print('Geeks:', re.search(r'\bGeeks\b', 'Geeks')) 
print('GeeksforGeeks:', re.search(r'\bGeeks\b', 'GeeksforGeeks')) 

#Output
Geeks: <_sre.SRE_Match object; span=(0, 5), match='Geeks'>
GeeksforGeeks: None

```

### Beginning and End of String
The ^ character chooses the beginning of a string and the $ character chooses the end of a string.

```
import re 


# Beginning of String 
match = re.search(r'^Geek', 'Campus Geek of the month') 
print('Beg. of String:', match) 

match = re.search(r'^Geek', 'Geek of the month') 
print('Beg. of String:', match) 

# End of String 
match = re.search(r'Geeks$', 'Compute science portal-GeeksforGeeks') 
print('End of String:', match) 

Output
Beg. of String: None
Beg. of String: <_sre.SRE_Match object; span=(0, 4), match='Geek'>
End of String: <_sre.SRE_Match object; span=(31, 36), match='Geeks'>

```

### Any Character
The . character represents any single character outside a bracketed character class.

```
import re 
  
print('Any Character', re.search(r'p.th.n', 'python 3'))

Output
Any Character <_sre.SRE_Match object; span=(0, 6), match='python'>

```

[Back](./README.md)
