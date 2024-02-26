# Assigning Values to Variables

## Direct Initialization Method
### Assign Values to Variables Direct Initialisation Method:

In Python, there is no need for explicit declaration in variables as compared to using some other programming languages. We can start using the variable right away.

```
# initialising variable directly
a = 5

# printing value of a
print ("The value of a is: " + str(a))

```
### Python Variables – Assign Multiple Values
Unlike other languages, we can easily assign values to multiple variables in python easily.

```
# Assigning multiple values in single line

a,b,c="geeks","for","geeks"
print(a+b+c)

```

## Assign Values to Variables Using Conditional Operator
This method is also called Ternary operators. So Basic Syntax of a Conditional Operator is:-

`condition? True_value : False_Value`

Using Conditional Operator, we can write one line code in python. The conditional operator works in such a way that first evaluates the condition, if the condition is true, the first expression( True_value) will print else evaluates the second expression(False_Value).

```
a = 1 if 20 > 10 else 0

# Printing value of a
print("The value of a is: " , str(a))

# This code is contributed by shivanisinghss2110

```

## Python One liner Conditional Statement Assigning
   
```
#one liner if-else
a = 1 if 20 > 10 else 0
 
# printing value of a
print ("The value of a is: " + str(a))

```