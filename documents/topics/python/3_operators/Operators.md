# Python Operators

In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for the purpose of logical and arithmetic operations. In this article, we will look into different types of Python operators. 

OPERATORS: These are the special symbols. Eg- + , * , /, etc.
OPERAND: It is the value on which the operator is applied.

## Arithmetic Operators in Python
Python Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication, and division.

In Python 3.x the result of division is a floating-point while in Python 2.x division of 2 integers was an integer. To obtain an integer result in Python 3.x floored (// integer) is used.

```
Operator	Description	Syntax
+	Addition: adds two operands	x + y
–	Subtraction: subtracts two operands	x – y
*	Multiplication: multiplies two operands	x * y
/	Division (float): divides the first operand by the second	x / y
//	Division (floor): divides the first operand by the second	x // y
%	Modulus: returns the remainder when the first operand is divided by the second	x % y
**	Power: Returns first raised to power second	x ** y
```

### Precedence of Arithmetic Operators in Python
The precedence of Arithmetic Operators in Python is as follows:

P – Parentheses
E – Exponentiation
M – Multiplication (Multiplication and division have the same precedence)
D – Division
A – Addition (Addition and subtraction have the same precedence)
S – Subtraction

## Comparison Operators in Python
In Python Comparison of Relational operators compares the values. It either returns True or False according to the condition.

```
Operator	Description	Syntax
>	Greater than: True if the left operand is greater than the right	x > y
<	Less than: True if the left operand is less than the right	x < y
==	Equal to: True if both operands are equal	x == y
!=	Not equal to – True if operands are not equal	x != y
>=	Greater than or equal to True if the left operand is greater than or equal to the right	x >= y
<=	Less than or equal to True if the left operand is less than or equal to the right	x <= y
```

### Precedence of Comparison Operators in Python
In Python, the comparison operators have lower precedence than the arithmetic operators. All the operators within comparison operators have the same precedence order.

## Logical Operators in Python
Python Logical operators perform Logical AND, Logical OR, and Logical NOT operations. It is used to combine conditional statements.

```
Operator	Description	Syntax
and	Logical AND: True if both the operands are true	x and y
or	Logical OR: True if either of the operands is true 	x or y
not	Logical NOT: True if the operand is false 	not x

```

### Precedence of Logical Operators in Python
The precedence of Logical Operators in Python is as follows:

Logical not
logical and
logical or


## Bitwise Operators in Python
Python Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

```
Operator	Description	Syntax
&	Bitwise AND	x & y
|	Bitwise OR	x | y
~	Bitwise NOT	~x
^	Bitwise XOR	x ^ y
>>	Bitwise right shift	x>>
<<	Bitwise left shift	x<<
```

### Precedence of Bitwise Operators in Python
The precedence of Bitwise Operators in Python is as follows:

Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR

## Assignment Operators in Python

Python Assignment operators are used to assign values to the variables.

```
Operator	Description	Syntax
=	Assign the value of the right side of the expression to the left side operand 	x = y + z
+=	Add AND: Add right-side operand with left-side operand and then assign to left operand	a+=b     a=a+b
-=	Subtract AND: Subtract right operand from left operand and then assign to left operand	a-=b     a=a-b
*=	Multiply AND: Multiply right operand with left operand and then assign to left operand	a*=b     a=a*b
/=	Divide AND: Divide left operand with right operand and then assign to left operand	a/=b     a=a/b
%=	Modulus AND: Takes modulus using left and right operands and assign the result to left operand	a%=b     a=a%b
//=	Divide(floor) AND: Divide left operand with right operand and then assign the value(floor) to left operand	a//=b     a=a//b
**=	Exponent AND: Calculate exponent(raise power) value using operands and assign value to left operand	a**=b     a=a**b
&=	Performs Bitwise AND on operands and assign value to left operand	a&=b     a=a&b
|=	Performs Bitwise OR on operands and assign value to left operand	a|=b     a=a|b
^=	Performs Bitwise xOR on operands and assign value to left operand	a^=b     a=a^b
>>=	Performs Bitwise right shift on operands and assign value to left operand	a>>=b     a=a>>b
<<=	Performs Bitwise left shift on operands and assign value to left operand	a <<= b     a= a << b
```

## Identity Operators in Python
In Python, is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

is          True if the operands are identical 
is not      True if the operands are not identical 

```
a = 10
b = 20
c = a 

print(a is not b) 
print(a is c)

Output
True
True

```

## Membership Operators in Python
In Python, in and not in are the membership operators that are used to test whether a value or variable is in a sequence.

in            True if value is found in the sequence
not in        True if value is not found in the sequence

```
x = 24
y = 20
list = [10, 20, 30, 40, 50] 

if (x not in list): 
	print("x is NOT present in given list") 
else: 
	print("x is present in given list") 

if (y in list): 
	print("y is present in given list") 
else: 
	print("y is NOT present in given list") 

Output
x is NOT present in given list
y is present in given list

```

## Ternary Operator in Python
in Python, Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5. 

It simply allows testing a condition in a single line replacing the multiline if-else making the code compact.

`Syntax :  [on_true] if [expression] else [on_false] `

### Examples of Ternary Operator in Python
The code assigns values to variables ‘a’ and ‘b’ (10 and 20, respectively). It then uses a conditional assignment to determine the smaller of the two values and assigns it to the variable ‘min’. Finally, it prints the value of ‘min’, which is 10 in this case.

 
```
a, b = 10, 20
min = a if a < b else b 

print(min) 

Output: 
10

```

[Back](./README.md)
