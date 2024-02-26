# Input in python:

* When input() function executes program flow will be stopped until the user has given input.
* The text or message displayed on the output screen to ask a user to enter an input value is optional i.e. the prompt, which will be printed on the screen is optional.
* Whatever you enter as input, the input function converts it into a string. if you enter an integer value still input() function converts it into a string. You need to explicitly convert it into an integer in your code using typecasting. 


```
# Program to check input 
# type in Python 

num = input ("Enter number :") 
print(num) 
name1 = input("Enter name : ") 
print(name1) 

# Printing type of input value 
print ("type of number", type(num)) 
print ("type of name", type(name1)) 

```

##  Typecasting the input to Integer:

There might be conditions when you might require integer input from the user/Console, the following code takes two input(integer/float) from the console and typecasts them to an integer then prints the sum. 

```
# input
num1 = int(input())
num2 = int(input())

# printing the sum in integer
print(num1 + num2)

```
## Typecasting the input to String:
All kinds of input can be converted to string type whether they are float or integer. We make use of keyword str for typecasting. 

 we can also take input string by just writing input() function by default it makes the input string

 ```
# input
string = str(input())

# output
print(string)

# Or by default
string_default = input()

# output
print(string_default)

 ```