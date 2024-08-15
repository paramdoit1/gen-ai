x = ['apple', 'orange', 'banana']

#Accessing items in the list
print(x[1])
#orange

print(f'I like the fruits {x[0]} and {x[1]}')
#I like the fruits apple and orange

print(x[-1])
#banana

print(x[0:2])
#['apple', 'banana']

print(x[1:])
# ['orange', 'banana']

print(x[:1])
#['apple']

if 'apple' in x:
    print('Apple in the list')
#Apple in the list

#Updating elements of list

x[1] = 'watermelon'
print(x)
#['apple', 'watermelon', 'banana']

x[0:2] = ['pineapple', 'cherry']
print(x)
#['pineapple', 'cherry', 'banana']

#To add an item at the end of the list
x.append('orange')
print(x)
# ['pineapple', 'cherry', 'banana', 'orange']

#To insert an item at specific index
x.insert(1, 'apple')
print(x)
#['pineapple', 'apple', 'cherry', 'banana', 'orange']

#Append the elements from other list
x1 = ['pineapple', 'apple', 'cherry']
x2 = ['banana', 'grape']

x1.extend(x2)
print(x1)
#['pineapple', 'apple', 'cherry', 'banana', 'orange']

#Loop through elements of the list
for item in x1:
    print(item)

'''
pineapple
apple
cherry
banana
grape
'''

#Loop through the list items by referring to their index numbers
#use range() and len() functions to create a suitable iterable

for i in range(len(x1)):
    print(x1[i])

'''
pineapple
apple
cherry
banana
grape
'''

#Looping using the while loop and run till the condition is true.

i=0
while(i<len(x1)):
    print(x1[i])
    i=i+1

'''
pineapple
apple
cherry
banana
grape
'''
#List Comprehension

[print('List Comprehension: ', item) for item in x1]

'''
List Comprehension:  pineapple
List Comprehension:  apple
List Comprehension:  cherry
List Comprehension:  banana
List Comprehension:  grape
'''


#Create a new list which has 'a' in fruit names
#Syntax: newlist = [expression for item in iterable if condition == True]

new_list = [fruit for fruit in x1 if 'a' in fruit]
print('The list with letter a is : ', new_list)

"""
The list with letter a is :  ['pineapple', 'apple', 'banana', 'grape']
"""

#creating a new list which does not have a

new_list = [fruit for fruit in x1 if 'a' not in fruit]
print('The list without letter a is : ', new_list)
#The list without letter a is :  ['cherry']

#creating a new list with fruit in upper case
new_list = [fruit.upper() for fruit in x1]
print('The list with fruit in upper case is : ', new_list)
#The list with fruit in upper case is :  ['PINEAPPLE', 'APPLE', 'CHERRY', 'BANANA', 'GRAPE']


#Iterate 20 numbers but print only numbers till 10 and that is odd.
new_list = [i for i in range(20) if i < 10 and i%2!=0]
print('Odd numbers till 10: ', new_list)
#Odd numbers till 10:  [1, 3, 5, 7, 9]

#Replace all apple with red apple
new_list = [fruit if fruit!='apple' else 'red apple' for fruit in x1]
print('New Fruit List: ', new_list)
#New Fruit List:  ['pineapple', 'red apple', 'cherry', 'banana', 'grape']

#Sorting he fruit
new_list.sort()
print('New Fruit List: ', new_list)
#New Fruit List:  ['banana', 'cherry', 'grape', 'pineapple', 'red apple']

#Sort in reverse order
new_list.sort(reverse=True)
print('New Fruit List in reverse order: ', new_list)
#New Fruit List in reverse order:  ['red apple', 'pineapple', 'grape', 'cherry', 'banana']

#Remove specific item
new_list.remove("grape")
print('New Fruit List: ', new_list)
#New Fruit List:  ['red apple', 'pineapple', 'cherry', 'banana']

#Copying List with copy method   
new_list = x1.copy()
print('New List with copy is : ', new_list)
#New List with copy is :  ['pineapple', 'apple', 'cherry', 'banana', 'grape']

#Copying List with list method   
new_list = list(x1)
print('New List with List is : ', new_list)
#New List with List is :  ['pineapple', 'apple', 'cherry', 'banana', 'grape']

#creating new List with :   
new_list = x1[:]
print('New List with : is : ', new_list)
# New List with : is :  ['pineapple', 'apple', 'cherry', 'banana', 'grape']

#removing item with specific index using pop method
new_list.pop(1)
print('New List after pop is : ', new_list)
#New List after pop is :  ['pineapple', 'cherry', 'banana', 'grape']

#removing item with specific index using del
del new_list[1]
print('New List after del is : ', new_list)

#New List after del is :  ['pineapple', 'banana', 'grape']

#emptying the list
new_list.clear()
print('New List after clear is : ', new_list)
#New List after clear is :  []

#del removes the list
del new_list
#print(' List after del is : ', new_list)
# --> 187 print(' List after del is : ', new_list)
#NameError: name 'new_list' is not defined

#Concatinate or combine two list
a1 = [1,2,3]
b1 = [4, 5, 6]
c1 = a1 +b1
print ('c1: ', c1)
#c1:  [1, 2, 3, 4, 5, 6]

#adding elements one by one

a1 = [1,2,3]
b1 = [4, 5, 6]
for b1_item in b1:
    a1.append(b1_item+10)

print('new list after append', a1)
#new list after append [1, 2, 3, 14, 15, 16]

#Creating new list using append
a1 = [1,2,3]
b1 = [4, 5, 6]
a1.extend(b1)
print('new list after append', a1)
#new list after append [1, 2, 3, 4, 5, 6]

  