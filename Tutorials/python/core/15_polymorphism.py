# The word polymorphism means "many forms" and in programming it refers to methods/functions/operators with the
#same name that can be executed on many objects and classes.

#An example, of a python function is that can be ised on different objects is len() function

x = "hello world"
print ('The length of the string is ', len(x))

x1= ['apple', 'orange', 'banana']
print ('The length of the list is ', len(x1))

car_dict = {
    "brand" : "ford",
    "model": "accord",
    "year": 2000
}
print ('The length of the dict is ', len(car_dict))

'''
The length of the string is  11
The length of the list is  3
The length of the dict is  3   
'''

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print('Move')
    
class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print('sail')

class Plane(Vehicle):
    def move(self):
        print('fly')

car1 = Car('Honda', 'Accord')
boat1 = Boat('Boater', 'Tourister')
plane1 = Plane('AirBus', 'A380')

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

'''
Honda
Accord
Move
Boater
Tourister
sail
AirBus
A380
fly
'''