# Boolean Data Type in Python
Data type with one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true), and those equal to False are falsy (false). However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by the class bool. 

Note – True and False with capital ‘T’ and ‘F’ are valid booleans otherwise python will throw an error. 

Example: The first two lines will print the type of the boolean values True and False, which is <class ‘bool’>. The third line will cause an error, because true is not a valid keyword in Python. Python is case-sensitive, which means it distinguishes between uppercase and lowercase letters. You need to capitalize the first letter of true to make it a boolean value.

```
print(type(True)) 
print(type(False)) 

print(type(true)) 

# Output:

<class 'bool'>
<class 'bool'>
```