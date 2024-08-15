# Tuples are used to store multiple items in a single variable
# The tuple is a collection which is ordered and unchangable
# and it allows duplicates

# Accessing elements of tuples
x_1 = ('apple', 'banana', 'orange')
print(x_1[1])
#banana

print(x_1[-1])
#orange

print(x_1[0:2])
#('apple', 'banana')

print(x_1[1:])
#('banana', 'orange')

#change value of Tuples
# Once a tuple is created, we cannot change its values. Tuples are unchangeable, or immutable.
# But as a work around,we can convert the tuple into a list, change the list, and convert list back to a tuple.

#Add elements to a tuple
y_1 = list(x_1)
y_1.append('grapes') 
x_1 = tuple(y_1)
print(x_1)
#('apple', 'banana', 'orange', 'grapes')

#Update elements in a list
y_1[1]='strawberry'
x_1 = tuple(y_1)
print(x_1)
#('apple', 'strawberry', 'orange', 'grapes')

#Adding 2 tuples
x_2 = ('apple', 'banana', 'orange')
y_2 = ('strawberry', )
#when creating a tuple with one item need to add a comma at the end

z_3 = x_2 + y_2
print(z_3)
#('apple', 'banana', 'orange', 'strawberry')

#Unpacking
x_2 = ('apple', 'banana', 'orange')
(red, yellow, green) = x_2
print(red, yellow, green)
#apple banana orange

#Using for loop
for item in x_2:
    print(item)

#apple
#banana
#orange

#Loop using for index
for i in range(len(x_2)):
    print(x_2[i])

#apple
#banana
#orange

#Loop using while with index

i = 0
while(i < len(x_2)):
    print(x_2[i])
    i = i +1

#apple
#banana
#orange

#Creating a new tuple with +
a1= (1,2,3)
a2=(4,5,6)
a3 = a1+a2
print(a3)
#(1, 2, 3, 4, 5, 6)

#Creating new tuple with *
a4 = a1 * 2
print(a4)
#(1, 2, 3, 1, 2, 3)
