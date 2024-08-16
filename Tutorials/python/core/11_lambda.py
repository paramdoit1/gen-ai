#Lambda function is a small anonymous function which can take any 
# number of arguments but can have only one expression.

#Syntax: lambda arguments: expression

#Lambda with single argument
x = lambda a : a+5
print(x(3))
# 8

#Lambda with multiple arguments
x1 = lambda a, b: a+b
print(x1(4,6))
#8

#Lambda functions: anonymous function inside another function

def myfunction(n):
    return lambda a : a*n

mydoubler = myfunction(2)
result = mydoubler(4)
print("Lambda function for double: ", result)
# Lambda functon for double:  8

mytripler = myfunction(3)
result = mytripler(4)
print("Lambda function for triple: ", result)
#Lambda function for triple:  12