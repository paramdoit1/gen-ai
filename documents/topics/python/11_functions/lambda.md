# Python lambda
## Introduction:
In Python, an anonymous function means that a function is without a name. As we already know that def keyword is used to define the normal functions and the lambda keyword is used to create anonymous functions.

## Python lambda Syntax:
lambda arguments : expression

## Python lambda Example:

```
calc = lambda num: "Even number" if num % 2 == 0 else "Odd number"

print(calc(20))

# Output:

Even number

```
## Python lambda properties:
* This function can have any number of arguments but only one expression, which is evaluated and returned.
* One is free to use lambda functions wherever function objects are required.
* You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
* It has various uses in particular fields of programming, besides other types of expressions in functions.

###  Example 1: Program to demonstrate return type of Python lambda keyword 
```
string = 'GeeksforGeeks'

# lambda returns a function object
print(lambda string: string)

# Output
<function <lambda> at 0x7fd7517ade18>
```
Explanation: In this above example, the lambda is not being called by the print function, but simply returning the function object and the memory location where it is stored. So, to make the print to print the string first, we need to call the lambda so that the string will get pass the print.

### Example 2: Invoking lambda return value to perform various operations
Here we have passed various types of arguments into the different lambda functions and printed the result generated from the lambda function calls.

```
filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
print("filter_nums():", filter_nums("Geeks101"))

do_exclaim = lambda s: s + '!'
print("do_exclaim():", do_exclaim("I am tired"))

find_sum = lambda n: sum([int(x) for x in str(n)])
print("find_sum():", find_sum(101))

# Output:

filter_nums(): Geeks
do_exclaim(): I am tired!
find_sum(): 2

```

### Example 3: Difference between lambda and normal function call
The main difference between lambda function and other functions defined using def keyword is that, we cannot use multiple statements inside a lambda function and allowed statements are also very limited inside lambda statements. Using lambda functions to do complex operations may affect the readability of the code.

```
def cube(y):
	print(f"Finding cube of number:{y}")
	return y * y * y


lambda_cube = lambda num: num ** 3

# invoking simple function
print("invoking function defined with def keyword:")
print(cube(30))
# invoking lambda function
print("invoking lambda function:", lambda_cube(30))

#Output:
invoking function defined with def keyword:
Finding cube of number:30
27000
invoking lambda function: 27000

```

### Example 4: The lambda function gets more helpful when used inside a function.
We can use lambda function inside map(), filter(), sorted() and many other functions. Here, we have demonstrated how to use lambda function inside some of the most common Python functions.

```
l = ["1", "2", "9", "0", "-1", "-2"]
# sort list[str] numerically using sorted()
# and custom sorting key using lambda
print("Sorted numerically:",
	sorted(l, key=lambda x: int(x)))

# filter positive even numbers
# using filter() and lambda function
print("Filtered positive even numbers:", 
	list(filter(lambda x: not (int(x) % 2 == 0 and int(x) > 0), l)))

# added 10 to each item after type and
# casting to int, then convert items to string again
print("Operation on each item using lambda and map()",
	list(map(lambda x: str(int(x) + 10), l)))

# Output
Sorted numerically: ['-2', '-1', '0', '1', '2', '9']
Filtered positive even numbers: ['1', '9', '0', '-1', '-2']
Operation on each item using lambda and map() ['11', '12', '19', '10', '9', '8']

```

### using mylist:
In this example, we define a lambda function that takes an argument x and adds 10 to it. We then use the map() function to apply the lambda function to each element in the list my_list. Finally, we convert the result to a list and print it.

Here’s another example that uses a lambda function to filter out even numbers from a list:

```
# Example list
my_list = [1, 2, 3, 4, 5]

# Use lambda to filter out even numbers from the list
new_list = list(filter(lambda x: x % 2 != 0, my_list))

# Print the new list
print(new_list)
#Output
[1, 3, 5]

```

`Approach:`

Define a list ‘my_list’ with some numbers.
Use lambda function with filter to check whether a number in the list is even or not.
Convert the filter object into a list using the list() function and store it in a new_list.
Print the new list with odd numbers.

[Back](./README.md)