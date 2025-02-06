# Global and Local Variables in Python
`Python Global variables` are those which are not defined inside any function and have a global scope whereas `Python local variables` are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function. 

## Python Local Variables
Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function. Let’s see how to create a local variable.

### Creating local variables in Python
Defining and accessing local variables

```
def f():

	# local variable
	s = "I love Geeksforgeeks"
	print(s)


# Driver code
f()
# Output
I love Geeksforgeeks

```
## Can a local variable be used outside a function?

If we will try to use this local variable outside the function then let’s see what will happen.

```
def f():
	
	# local variable
	s = "I love Geeksforgeeks"
	print("Inside Function:", s)

# Driver code
f()
print(s)

# Output:

NameError: name 's' is not defined
```

## Python Global Variables
These are those which are defined outside any function and which are accessible throughout the program, i.e., inside and outside of every function. Let’s see how to create a Python global variable.

### Create a global variable  in Python
Defining and accessing Python global variables.

```
# This function uses global variable s
def f():
	print("Inside Function", s)

# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)

# Output
Inside Function I love Geeksforgeeks
Outside Function I love Geeksforgeeks

```

The variable s is defined as the global variable and is used both inside the function as well as outside the function.

Note: As there are no locals, the value from the globals will be used but make sure both the local and the global variables should have same name.

## Why do we use Local and Global variables in Python?
Now, what if there is a Python variable with the same name initialized inside a function as well as globally? Now the question arises, will the local variable will have some effect on the global variable or vice versa, and what will happen if we change the value of a variable inside of the function f()? Will it affect the globals as well? We test it in the following piece of code: 

`Example`

If a variable with the same name is defined inside the scope of the function as well then it will print the value given inside the function only and not the global value. 

```
# This function has a variable with
# name same as s.
def f():
	s = "Me too."
	print(s)

# Global scope
s = "I love Geeksforgeeks"
f()
print(s)

#Output
Me too.
I love Geeksforgeeks

```

## The global Keyword
We only need to use the global keyword in a function if we want to do assignments or change the global variable. global is not needed for printing and accessing. Python “assumes” that we want a local variable due to the assignment to s inside of f(), so the first statement throws the error message. Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example: 

### Example 1: Using Python global keyword

```
# This function modifies the global variable 's'
def f():
	global s
	s += ' GFG'
	print(s)
	s = "Look for Geeksforgeeks Python Section"
	print(s) 

# Global Scope
s = "Python is great!"
f()
print(s)


Python Tutorial
Introduction
Python Input/Output
Python Operators
Python Data Types
Python String
Python RegEx
Python List
Python Tuples
Python Sets
Python Dictionary
Python Control Flow
Python Functions
Python Functions
*args and **kwargs in Python
When to use yield instead of return in Python?
Generators in Python
Python lambda
Global and Local Variables in Python
Global keyword in Python
First Class functions in Python
Python Closures
Decorators in Python
Decorators with parameters in Python
Memoization using decorators in Python
Python OOP
Python Exception Handling
Python File handling
Advanced Python Tutorials
Python API Tutorial: Getting Started with APIs
Python Automation Tutorial
Python Projects - Beginner to Advanced
Python Programs
Top 50+ Python Interview Questions and Answers (Latest 2024)
Python Cheat Sheet (2023)
Python JSON
Free Python Course Online [2024]
Global and Local Variables in Python
Read
Courses
Practice
Video
Python Global variables are those which are not defined inside any function and have a global scope whereas Python local variables are those which are defined inside a function and their scope is limited to that function only. In other words, we can say that local variables are accessible only inside the function in which it was initialized whereas the global variables are accessible throughout the program and inside every function. 

Python Local Variables
Local variables in Python are those which are initialized inside a function and belong only to that particular function. It cannot be accessed anywhere outside the function. Let’s see how to create a local variable.

Creating local variables in Python
Defining and accessing local variables

   
def f():
 
    # local variable
    s = "I love Geeksforgeeks"
    print(s)
 
 
# Driver code
f()

Output
I love Geeksforgeeks
Can a local variable be used outside a function?


If we will try to use this local variable outside the function then let’s see what will happen.

   
def f():
     
    # local variable
    s = "I love Geeksforgeeks"
    print("Inside Function:", s)
 
# Driver code
f()
print(s)
Output:

NameError: name 's' is not defined
Python Global Variables
These are those which are defined outside any function and which are accessible throughout the program, i.e., inside and outside of every function. Let’s see how to create a Python global variable.


Create a global variable  in Python
Defining and accessing Python global variables.

   
# This function uses global variable s
def f():
    print("Inside Function", s)
 
# Global scope
s = "I love Geeksforgeeks"
f()
print("Outside Function", s)

Output
Inside Function I love Geeksforgeeks
Outside Function I love Geeksforgeeks
The variable s is defined as the global variable and is used both inside the function as well as outside the function.

Note: As there are no locals, the value from the globals will be used but make sure both the local and the global variables should have same name.

Why do we use Local and Global variables in Python?
Now, what if there is a Python variable with the same name initialized inside a function as well as globally? Now the question arises, will the local variable will have some effect on the global variable or vice versa, and what will happen if we change the value of a variable inside of the function f()? Will it affect the globals as well? We test it in the following piece of code: 

Example

If a variable with the same name is defined inside the scope of the function as well then it will print the value given inside the function only and not the global value. 


   
# This function has a variable with
# name same as s.
def f():
    s = "Me too."
    print(s)
 
# Global scope
s = "I love Geeksforgeeks"
f()
print(s)

Output
Me too.
I love Geeksforgeeks
Now, what if we try to change the value of a global variable inside the function? Let’s see it using the below example.

 
# This function uses global variable s
def f():
    s += 'GFG'
    print("Inside Function", s)
 
 
# Global scope
s = "I love Geeksforgeeks"
f()
Output:

UnboundLocalError: local variable 's' referenced before assignment
To make the above program work, we need to use the “global” keyword in Python. Let’s see what this global keyword is.

The global Keyword
We only need to use the global keyword in a function if we want to do assignments or change the global variable. global is not needed for printing and accessing. Python “assumes” that we want a local variable due to the assignment to s inside of f(), so the first statement throws the error message. Any variable which is changed or created inside of a function is local if it hasn’t been declared as a global variable. To tell Python, that we want to use the global variable, we have to use the keyword “global”, as can be seen in the following example: 

Example 1: Using Python global keyword

   
# This function modifies the global variable 's'
def f():
    global s
    s += ' GFG'
    print(s)
    s = "Look for Geeksforgeeks Python Section"
    print(s) 
 
# Global Scope
s = "Python is great!"
f()
print(s)

# Output
Python is great! GFG
Look for Geeksforgeeks Python Section
Look for Geeksforgeeks Python Section

```
### Example 2: Using Python global and local variables

```
a = 1

# Uses global because there is no local 'a'
def f():
	print('Inside f() : ', a)

# Variable 'a' is redefined as a local
def g():
	a = 2
	print('Inside g() : ', a)

# Uses global keyword to modify global 'a'
def h():
	global a
	a = 3
	print('Inside h() : ', a)


# Global scope
print('global : ', a)
f()
print('global : ', a)
g()
print('global : ', a)
h()
print('global : ', a)

# Output
global :  1
Inside f() :  1
global :  1
Inside g() :  2
global :  1
Inside h() :  3
global :  3

```

## Difference b/w Local Variable Vs. Global Variables
Comparision Basis	Global Variable	Local Variable
`Definition`	declared outside the functions	declared within the functions
`Lifetime`	They are created  the execution of the program begins and are lost when the program is ended	They are created when the function starts its execution and are lost when the function ends
`Data Sharing`	Offers Data Sharing	It doesn’t offers Data Sharing
`Scope`	Can be access throughout the code	Can access only inside the function
`Parameters needed`	parameter passing is not necessary	parameter passing is necessary
`Storage`	 A fixed location selected by the compiler	They are  kept on the stack
`Value`	Once the value changes it is reflected throughout the code	once changed the variable don’t affect other functions of the program

[Back](./README.md)






