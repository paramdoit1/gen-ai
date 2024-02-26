# Numeric Data Types in Python
The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, or even a complex number. These values are defined as Python int, Python float, and Python complex classes in Python.

`Integers` – This value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). In Python, there is no limit to how long an integer value can be.
`Float` – This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
`Complex Numbers` – A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j. For example – 2+3j
Note – type() function is used to determine the type of data type. 

Example: This code demonstrates how to determine the data type of variables in Python using the type() function. It prints the data types of three variables: a (integer), b (float), and c (complex). The output shows the respective data types for each variable.

```
a = 5
print("Type of a: ", type(a)) 

b = 5.0
print("\nType of b: ", type(b)) 

c = 2 + 4j
print("\nType of c: ", type(c))
# Output:

Type of a:  <class 'int'>
Type of b:  <class 'float'>
Type of c:  <class 'complex'>
```

    