#Creating a function
def operations():
    print('Operations is invoked')

operations()
#Operations is invoked

#Arguments

def operations(name):
    print('Operations invoked is:', name)

operations('add')
operations('multiply')

#Operations invoked is: add
#Operations invoked is: multiply

#Number of arguments and return value
def name(fname, lname):
    fullName = fname +" " + lname
    return fullName

print('Name : ', name('Raja', 'Raman'))
# Name :  Raja Raman

#Arbitary arguments *args
def kidsName(*names):
    print('The last name of child is : ', names[2])
kidsName('Raju', 'Ravi', 'Kiran')
#The last name of child is :  Kiran

#Keyword arguments
def kidsName(name1, name2, name3):
    print('The last name of child is : ', name3)

kidsName(name2 = 'Raju', name1= 'Ravi', name3='Kiran')
#The last name of child is :  Kiran

#Arbitary keyword arguments, **kwargs
# If we dont know how many arguments, then add two asterisk 
# ** before the parameter name of the function.

def kidsName(**names):
    print('The last name of child is : ', names['name3'])

kidsName(name2 = 'Raju', name1= 'Ravi', name3='Kiran')
#The last name of child is :  Kiran

#Default parameter value

def getCountry(country = "India"):
    print('The country is : ', country)

getCountry('USA')
getCountry()

'''
The country is :  USA
The country is :  India
'''

#Passing list as arguments
def getFruitList(fruitsList):
    for fruit in fruitsList:
        print(fruit)

fruits = ['apple', 'orange', 'banana']

getFruitList(fruits)

'''
apple
orange
banana
'''

#Pass Statement
#Function definitions to avoid error add pass if there are no contents

def myFunction():
    pass