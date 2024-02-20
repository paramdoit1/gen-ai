# Python Keywords

There are a set of predefined words, called Keywords which along with Identifiers will form meaningful sentences when used together. Python keywords cannot be used as the names of variables, functions, and classes.


`import`	
It is used to import a module

`from`	
To import specific parts of a module

`class`	
It is used to define a class

`global`	
It is used to declare a global variable

`True` 	
Represents an expression that will result in true.

`False`	
Represents an expression that will result in not being true.

`and ` 	
It is a Logical Operator

`or`	
It is a Logical Operator

`not`	
It is a Logical Operator

`assert`	
It is used for debugging

`if`	
To create a Conditional Statement

`elif`	
Conditional statements, same as else-if

`else`	
It is used in a conditional statement

`for`	
It is used to create Loop

`while`	
While Loop is used to execute a block of statements

`continue`	
Skip the next iteration of a loop

`break`	
Break out a Loop

`pass`	
pass is used when the user doesn’t want any code to execute


`def`	
It is used to define the Function

`return`	
return is used to end the execution

`del`	
It is used to delete an object

`is	`
It is used to test if two variables are equal

`try`	
Try is used to handle errors

`except`	
try-except is used to handle these errors

`finally`	
It is used with exceptions

`raise`	
raise is used to raise exceptions or errors.

`in`	
To check if a value is present in a Tuple, List, etc.

`nonlocal`	
It is a non-local variable

`as`	
It is used to create an alias name

`lambda`	
Used to create an anonymous function

`with`	
 with statement is used in exception handling

`None`	
It represents a null value

`yield`	
yield keyword is used to create a generator function

## Getting the List of all Python keywords

```
import keyword
 
# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)

```

### True, False, None Keyword in Python
`True:` This keyword is used to represent a boolean true. If a statement is true, “True” is printed.
`False:` This keyword is used to represent a boolean false. If a statement is false, “False” is printed. 
`None:` This is a special constant used to denote a null value or a void. It’s important to remember, 0, any empty container(e.g. empty list) does not compute to None. 
It is an object of its datatype – NoneType. It is not possible to create multiple None objects and can assign them to variables.

* False is 0, and True is 1.
* True + True + True is 3.
* True + False + False is 1.
* None isn’t equal to 0 or an empty list ([]).
   

```
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])

`Output`
True
True
3
1
False
False

```

### and, or, not, in, is In Python

#### Python and Keyword
This a logical operator in Python. “and” Return the first false value. If not found return last. The truth table for “and” is depicted below. 

|    A     |    B    | A and B |
| -------- | ------- | ------- |
| True     | True    |  True   | 
| True     | False   |  False  |
| False    | True    |  False  |
| False    | False   |  False  |

3 and 0 return 0 
3 and 10 return 10

#### Python or Keyword
This a logical operator in Python. “or” Return the first True value. if not found return last. The truth table for “or” is depicted below. 

|    A     |    B    | A or B |
| -------- | ------- | ------- |
| True     | True    |  True   | 
| True     | False   |  True   |
| False    | True    |  True   |
| False    | False   |  False  |

3 or 0 returns 3 
3 or 10 returns 3

### Python not keyword:

The not operator is the Boolean or logical operator that implements negation in Python. It’s unary, which means that it takes only one operand. The operand can be a Boolean expression or any Python object. Even user-defined objects work. The task of not is to reverse the truth value of its operand.

If you apply not to an operand that evaluates to True, then you get False as a result. If you apply not to a false operand, then you get True:

|    A     | not A   | 
| -------- | ------- |
| True     | False   | 
| False    | True    |  

```

>>> x = 2
>>> y = 5

>>> x > y
False

>>> not x > y
True

```
### Python in Keyword

The ‘in’ keyword in Python returns True if a certain element is present in a Python object, else it will return False. It has two purposes:

To check if a value is present in a list, tuple, range, string, etc.
To iterate through a sequence in a for loop.

The in keyword in Python can be used with if statements as well as with for loops. It has the following syntax:

```
# Using if statement
if element in sequence:
    # statement

# Using for statement
for element in sequence:
    # statement
```

#### “in” Keyword with Python if Statement
In this example, we will create a Python list of animals. Then we will use the in keyword with the if statement to check the presence of “lion” in animals.

```
# Python program to demonstrate 
# in keyword 

# Create a list 
animals = ["dog", "lion", "cat"] 

# Check if lion in list or not 
if "lion" in animals: 
	print("Yes")
```

Output:
`Yes`

#### Use of in keyword in for loop in Python

In this example, we will first define a Python String, and use for loop to iterate over each character in that string.

```
# Python program to demonstrate 
# in keyword 

# Create a string 
s = "GeeksforGeeks"

# Iterating through the string 
for i in s: 
	
	# if f occurs in the string 
	# break the loop 
	if i == 'f': 
		break
	
	print(i) 

```
```
Output:

G
e
e
k
s

```

### Python is Keyword
The “is” keyword in Python is used to test object identity. The “is keyword” is used to test whether two variables belong to the same object. The test will return True if the two objects are the same else it will return False even if the two objects are 100% equal.

```
# Python program to demonstrate
# is keyword
 
x = 10
y = 10
 
if x is y:
    print(True)
else:
    print(False)

```

### Iteration Keywords: for, while, break, continue, else
#### The for Keyword:
The most common loop in Python is the for loop. It’s constructed by combining the Python keywords for and in explained earlier. The basic syntax for a for loop is as follows:

```
for <element> in <container>:
    <statements>
```

Example:

```
>>> for num in range(1, 6):
      print(num)
```

```
>>> people = ["Kevin", "Creed", "Jim"]
>>> for person in people:
      print(f"{person} was in The Office.")
```
#### The while Keyword:

Python’s while loop uses the keyword while and works like a while loop in other programming languages. As long as the condition that follows the while keyword is truthy, the block following the while statement will continue to be executed over and over again:

```
while <expr>:
    <statements>
```
Example:

```
>>> while True:
      print("working...")
```

#### The break Keyword
If you need to exit a loop early, then you can use the break keyword. This keyword will work in both for and while loops:

```
for <element> in <container>:
    if <expr>:
        break
```

Example:

```
>>> nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> total_sum = 0
>>> for num in nums:
      total_sum += num
      if total_sum > 10:
        break

>>> total_sum
15
```

#### The continue Keyword

Python also has a continue keyword for when you want to skip to the next loop iteration. Like in most other programming languages, the continue keyword allows you to stop executing the current loop iteration and move on to the next iteration:

```
for <element> in <container>:
    if <expr>:
        continue
```
The continue keyword also works in while loops. If the continue keyword is reached in a loop, then the current iteration is stopped, and the next iteration of the loop is started.

### Control Flow Keywords: if, elif, else
Three Python keywords are used for control flow: if, elif, and else. These Python keywords allow you to use conditional logic and execute code given certain conditions. These keywords are very common—they’ll be used in almost every program you see or write in Python.

#### The if Keyword
The if keyword is used to start a conditional statement. An if statement allows you to write a block of code that gets executed only if the expression after if is truthy.

The syntax for an if statement starts with the keyword if at the beginning of the line, followed by a valid expression that will be evaluated for its truthiness value:

```
if <expr>:
    <statements>
```

```
if <expr2>:
    <var> = <expr1>
else:
    <var> = <expr3>
```
#### The elif Keyword
The elif statement looks and functions like the if statement, with two major differences:

* Using elif is only valid after an if statement or another elif.
* We can use as many elif statements as you need.

In other programming languages, elif is either else if (two separate words) or elseif (both words mashed together). When you see elif in Python, think else if:

```
if <expr1>:
    <statements>
elif <expr2>:
    <statements>
elif <expr3>:
    <statements>
```

#### The else Keyword
The else statement, in conjunction with the Python keywords if and elif, denotes a block of code that should be executed only if the other conditional blocks, if and elif, are all falsy:

```
if <expr>:
    <statements>
else:
    <statements>
```

### Structure Keywords: def, class, with, as, pass, lambda
#### The def Keyword
Python’s keyword def is used to define a function or method of a class. This is equivalent to function in JavaScript and PHP. The basic syntax for defining a function with def looks like this:

def <function>(<params>):
    <body>

Example:

```
def fun():
    print("Inside Function")
 
fun()
```

#### The class Keyword
To define a class in Python, you use the class keyword. The general syntax for defining a class with class is as follows:

```
class MyClass(<extends>):
    <body>
```

Example:

```
class Dog:
	attr1 = "mammal"
	attr2 = "dog"

	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()

```

#### With in Python:

This code demonstrates how to use the with statement to open a file named 'file_path' in write mode ('w'). It writes the text 'hello world !' to the file and automatically handles the opening and closing of the file. The with statement is used for better resource management and ensures that the file is properly closed after the block is executed.


Example:

```
# using with statement
with open('file_path', 'w') as file:
	file.write('hello world !')

```
#### The pass Keyword
Since Python doesn’t have block indicators to specify the end of a block, the pass keyword is used to specify that the block is intentionally left blank. It’s the equivalent of a no-op, or no operation. Here are a few examples of using pass to specify that the block is blank:

Example:

```
def my_function():
    pass

class MyClass:
    pass

if True:
    pass
```

#### The lambda Keyword
The lambda keyword is used to define a function that doesn’t have a name and has only one statement, the results of which are returned. Functions defined with lambda are referred to as lambda functions:

A basic example of a lambda function that computes the argument raised to the power of 10 would look like this:

`p10 = lambda x: x**10`

This is equivalent to defining a function with def:

```
def p10(x):
    return x**10
```

### Import Keywords: import, from, as

####  The import Keyword
Python’s import keyword is used to import, or include, a module for use in your Python program. Basic usage syntax looks like this:

` import <module>`

For example, if you want to use the Counter class from the collections module in the standard library, then you can use the following code:

```
>>> import collections
>>> collections.Counter()
Counter()
```
Importing collections in this way makes the whole collections module, including the Counter class, available to your program. By using the module name, you have access to all the tools available in that module. To get access to Counter, you reference it from the module: collections.Counter.


#### The from Keyword
The from keyword is used together with import to import something specific from a module:

```
from <module> import <thing>
```

This will import whatever <thing> is inside <module> to be used inside your program. These two Python keywords, from and import, are used together.

If you want to use Counter from the collections module in the standard library, then you can import it specifically:

```
>>> from collections import Counter
>>> Counter()
Counter()
```
Importing Counter like this makes the Counter class available, but nothing else from the collections module is available. Counter is now available without you having to reference it from the collections module.

#### The as Keyword
The as keyword is used to alias an imported module or tool. It’s used together with the Python keywords import and from to change the name of the thing being imported:

```
import <module> as <alias>
from <module> import <thing> as <alias>
```

If you want to import the Counter class from the collections module but name it something different, you can alias it by using as:

```
>>> from collections import Counter as C
>>> C()
Counter()

```

```
import numpy as np
import pandas as pd
```
### Exception-Handling Keywords: try, except, raise, finally, else, assert
One of the most common aspects of any Python program is the raising and catching of exceptions. Because this is such a fundamental aspect of all Python code, there are several Python keywords available to help make this part of your code clear and concise.

### The try Keyword:

Any exception-handling block begins with Python’s try keyword. This is the same in most other programming languages that have exception handling.

The code in the try block is code that might raise an exception. Several other Python keywords are associated with try and are used to define what should be done if different exceptions are raised or in different situations. These are except, else, and finally

```
try:
    <statements>
<except|else|finally>:
    <statements>
```

A try block isn’t valid unless it has at least one of the other Python keywords used for exception handling as part of the overall try statement.

If you wanted to calculate and return the miles per gallon of gas (mpg) given the miles driven and the gallons of gas used, then you could write a function like the following:

The first problem you might see is that your code could raise a ZeroDivisionError if the gallons parameter is passed in as 0. The try keyword allows you to modify the code above to handle that situation appropriately:

```
def mpg(miles, gallons):
    try:
        mpg = miles / gallons
    except ZeroDivisionError:
        mpg = None
    return mpg
```

Now if gallons = 0, then mpg() won’t raise an exception and will return None instead. This might be better, or you might decide that you want to raise a different type of exception or handle this situation differently. You’ll see an expanded version of this example below to illustrate the other keywords used for exception handling.


#### The except Keyword
Python’s except keyword is used with try to define what to do when specific exceptions are raised. You can have one or more except blocks with a single try. The basic usage looks like this:

```
def mpg(miles, gallons):
    try:
        mpg = miles / gallons
    except ZeroDivisionError:
        mpg = None
    except TypeError as ex:
        print("you need to provide numbers")
        raise ex
    return mpg
```

Here, you modify mpg() to raise the TypeError exception only after you’ve printed a helpful reminder to the screen.

Notice that the except keyword can also be used in conjunction with the as keyword. This has the same effect as the other uses of as, giving the raised exception an alias so you can work with it in the except block.

#### The raise Keyword
The raise keyword raises an exception. If you find you need to raise an exception, then you can use raise followed by the exception to be raised:

```
raise <exception>
```

#### The finally Keyword
Python’s finally keyword is helpful for specifying code that should be run no matter what happens in the try, except, or else blocks. To use finally, use it as part of a try block and specify the statements that should be run no matter what:

Using the example from before, it might be helpful to specify that, no matter what happens, you want to know what arguments the function was called with. You could modify mpg() to include a finally block that does just that:

```
def mpg(miles, gallons):
    try:
        mpg = miles / gallons
    except ZeroDivisionError:
        mpg = None
    except TypeError as ex:
        print("you need to provide numbers")
        raise ex
    finally:
        print(f"mpg({miles}, {gallons})")
    return mpg
```

#### The else Keyword Used With try and except
You’ve learned that the else keyword can be used with both the if keyword and loops in Python, but it has one more use. It can be combined with the try and except Python 
keywords. You can use else in this way only if you also use at least one except block:

In this context, the code in the else block is executed only if an exception was not raised in the try block. In other words, if the try block executed all the code successfully, then the else block code would be executed.

In the mpg() example, imagine you want to make sure that the mpg result is always returned as a float no matter what number combination is passed in. One of the ways you could do this is to use an else block. If the try block calculation of mpg is successful, then you convert the result to a float in the else block before returning:

```
def mpg(miles, gallons):
    try:
        mpg = miles / gallons
    except ZeroDivisionError:
        mpg = None
    except TypeError as ex:
        print("you need to provide numbers")
        raise ex
    else:
        mpg = float(mpg) if mpg is not None else mpg
    finally:
        print(f"mpg({miles}, {gallons})")
    return mpg
```
#### The assert Keyword
The assert keyword in Python is used to specify an assert statement, or an assertion about an expression. An assert statement will result in a no-op if the expression (<expr>) is truthy, and it will raise an AssertionError if the expression is falsy. To define an assertion, use assert followed by an expression:

`assert <expr>`

Generally, assert statements will be used to make sure something that needs to be true is. You shouldn’t rely on them, however, as they can be ignored depending on how your Python program is executed.

Example:

```
x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"
```

### Variable Handling Keywords: del, global, nonlocal
Three Python keywords are used to work with variables. The del keyword is much more commonly used than the global and nonlocal keywords. But it’s still helpful to know and understand all three keywords so you can identify when and how to use them.

#### The del Keyword
del is used in Python to unset a variable or name. You can use it on variable names, but a more common use is to remove indexes from a list or dictionary. To unset a variable, use del followed by the variable you want to unset:

Let’s assume you want to clean up a dictionary that you got from an API response by throwing out keys you know you won’t use. You can do so with the del keyword:

```
>>> del response["headers"]
>>> del response["errors"]
```
This will remove the "headers" and "errors" keys from the dictionary response.

#### The global Keyword
If you need to modify a variable that isn’t defined in a function but is defined in the global scope, then you’ll need to use the global keyword. This works by specifying in the function which variables need to be pulled into the function from the global scope:

Example:

```
# global variable
a = 15
b = 10
 
# function to perform addition
def add():
    c = a + b
    print(c)
 
 
# calling a function
add()
```

```
a = 15
 
# function to change a global value
def change():
    # increment value of a by 5
    b = a + 5
    a = b
    print(a)
 
 
change()
Output:
UnboundLocalError: local variable 'a' referenced before assignment
```

```

x = 15
 
 
def change():
    # using a global keyword
    global x
 
    # increment value of a by 5
    x = x + 5
    print("Value of x inside a function :", x)
 
 
change()
print("Value of x outside a function :", x)

```

#### The nonlocal Keyword
The nonlocal keyword is similar to global in that it allows you to modify variables from a different scope. With global, the scope you’re pulling from is the global scope. With nonlocal, the scope you’re pulling from is the parent scope. The syntax is similar to global:

`nonlocal <variable>`

### Asynchronous Programming Keywords: async, await
async/await: two new Python keywords that are used to define coroutines

asyncio: the Python package that provides a foundation and API for running and managing coroutines

Parallelism consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

Concurrency is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

Threading is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL, but that’s beyond the scope of this article.

That leaves one more term. What does it mean for something to be asynchronous? This isn’t a rigorous definition, but for our purposes here, I can think of two properties:

Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
Asynchronous code, through the mechanism above, facilitates concurrent execution. To put it differently, asynchronous code gives the look and feel of concurrency.

#### The async/await Syntax and Native Coroutines

At the heart of async IO are coroutines. A coroutine is a specialized version of a Python generator function. Let’s start with a baseline definition and then build off of it as you progress here: a coroutine is a function that can suspend its execution before reaching return, and it can indirectly pass control to another coroutine for some time.

Later, you’ll dive a lot deeper into how exactly the traditional generator is repurposed into a coroutine. For now, the easiest way to pick up how coroutines work is to start making some.

Let’s take the immersive approach and write some async IO code. This short program is the Hello World of async IO but goes a long way towards illustrating its core functionality:


```

#!/usr/bin/env python3
# countasync.py

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

 Output:
 $ python3 countasync.py
One
One
One
Two
Two
Two
countasync.py executed in 1.01 seconds.    
```

At this point, a more formal definition of async, await, and the coroutine functions that they create are in order. This section is a little dense, but getting a hold of async/await is instrumental, so come back to this if you need to:

The syntax async def introduces either a native coroutine or an asynchronous generator. The expressions async with and async for are also valid, and you’ll see them later on.

The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, “Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, go let something else run.”

```
import asyncio
import time

async def count():
    print('Counting...')
    await asyncio.sleep(1)
    print('Done!')

start = time.time()
asyncio.run(count())
asyncio.run(count())
end = time.time()

print(f'Total time: {end - start}')

# Output:
# 'Counting...'
# (After a one-second pause) 'Done!'
# 'Counting...'
# (After a one-second pause) 'Done!'
# 'Total time: 2.0'

```
