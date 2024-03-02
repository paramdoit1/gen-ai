# Constructors in Python

## Introduction:
Constructors are generally used for instantiating an object. The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. In Python the __init__() method is called the constructor and is always called when an object is created.

## Types of constructors: 

`default constructor`: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
`parameterized constructor`: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.


```
class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()

# Output
GeekforGeeks

```

## Example of the parameterized constructor : 

```
class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()

# Output
First number = 1000
Second number = 2000
Addition of two numbers = 3000
First number = 10
Second number = 20
Addition of two numbers = 30
```

## Advantages of using constructors in Python:
`Initialization of objects`: Constructors are used to initialize the objects of a class. They allow you to set default values for attributes or properties, and also allow you to initialize the object with custom data.

`Easy to implement`: Constructors are easy to implement in Python, and can be defined using the __init__() method.

`Better readability`: Constructors improve the readability of the code by making it clear what values are being initialized and how they are being initialized.

`Encapsulation`: Constructors can be used to enforce encapsulation, by ensuring that the object’s attributes are initialized correctly and in a controlled manner.

## Disadvantages of using constructors in Python:
`Overloading not supported`: Unlike other object-oriented languages, Python does not support method overloading. This means that you cannot have multiple constructors with different parameters in a single class.

`Limited functionality`: Constructors in Python are limited in their functionality compared to constructors in other programming languages. For example, Python does not have constructors with access modifiers like public, private or protected.

`Constructors may be unnecessary`: In some cases, constructors may not be necessary, as the default values of attributes may be sufficient. In these cases, using a constructor may add unnecessary complexity to the code.

Overall, constructors in Python can be useful for initializing objects and enforcing encapsulation. However, they may not always be necessary and are limited in their functionality compared to constructors in other programming languages.

