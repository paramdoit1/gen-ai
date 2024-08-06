a = 4
b = 'Tree is green'

print(a, b)
# 4 Tree is green

print(type(a))
#<class 'int'>

print(type(b))
#<class 'int'>

#Assigning multiple values to variables
x, y, z ="Apple" , "Orange", "Banana"
print(x,y,z)

#Assigning one value to multiple variables
x1 = y1 = z1 ="Apple" 
print(x1,y1,z1)

#Apple Apple Apple

#Unpack variables
fruits = ["apple", "orange", "banana"]
m, n, o = fruits
print(m, n, o)
#apple orange banana

#Global Variables
a = "hello"

def myGreenWorld():
    a="world"
    print(a)

myGreenWorld()
print(a)

#world
#hello