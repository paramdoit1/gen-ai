   
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}: {self.age}"
    
class Student(Person):
    
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.height = height

    def welcomeMessage(self):
        return f'Welcome {self.name} with {self.age} and height {self.height} cm'
    
s1 = Student('Raja', 30, 150)
print(s1.welcomeMessage())

# Welcome Raja with 30 and height 150 cm

#super() function
# Python has super() function that will make the child class inherit all the methods
# and properties from its parent


    