# A class is a blueprint for creating objects
# Almost everything in python is a object, with its properties and objects

class Vehicle:
    x = 5

o1 = Vehicle()
print(o1.x)
#5

# The __init__() function

# __init__method in python is used to initialize objects if a class and also called as construtor
# Used to initialise the object state.The main task is to assign the values to the data members of the class, when the object is created.
# All classes have built in function called __init__() which is always executed when the class is being initiated.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sendMessage(self):
        return 'Hello : '+ self.name
    
p1 = Person('Ramu', 25)
print('Person name: ', p1.name)
print('Person age: ', p1.age)
print('Message: ', p1.sendMessage())

'''
Person name:  Ramu
Person age:  25
Message:  Hello : Ramu
'''

# __str__() function
# __str__() function controls what should returned when the class object is represented as a string


# Self parameter
# Self parameter is a reference to the current instance of the class and 
# is used to access variables that belongs to the class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}: {self.age}"
    
p1 = Person('Ramu', 25)
print(p1)
#Ramu: 25