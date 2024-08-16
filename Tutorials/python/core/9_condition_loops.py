# if condition

a = 10
b = 100

if b > a:
    print('B is greater')

#B is greater

# if elif condition

if a>b:
    print('A is greater than B')
elif b>80:
    print('B is greater than 80')
#B is greater than 80

if a>b:
    print('A is greater than B')
elif b>120:
    print('B is greater than 120')
else:
    print('B is less than 120 and B is greater than A')

#B is less than 120 and B is greater than A

#Short hand if
if(b>a): print('B is greater than A') 
#B is greater than A

#short hand if else
print('A is greater than B')  if(a>b) else  print('B is greater than A') 
#B is greater than A

#And
a=10
b=20
c=30

if (b>a) and (c>b):
    print('Both conditions are true')
#Both conditions are true

if (a>b) or (c>b):
    print('Either conditions are true')
#Either conditions are true

if not (a>b):
   print('B is greater')
#B is greater

# If statements cannot be empty. If no content add pass statement to avoid error
if not (a>b):
   pass

#While Loop

i = 0

while (i<5):
 print('The value of i is : ', i)
 i = i + 1

'''
The value of i is :  0
The value of i is :  1
The value of i is :  2
The value of i is :  3
The value of i is :  4
'''

i = 0

while (i<5):
 print('The value of i is : ', i)
 i = i + 1
else:
    print(' The value of i reached ', i)

'''
The value of i is :  0
The value of i is :  1
The value of i is :  2
The value of i is :  3
The value of i is :  4
The value of i reached  5
'''



# Skipping the specific iteration with continue

i = 0

while (i<5):
 i = i + 1
 if (i ==2):
     continue
 print('The value of i is : ', i)
else:
    print(' The value of i reached ', i)

'''
The value of i is :  0
The value of i is :  1
The value of i is :  3
The value of i is :  4
The value of i reached  5
'''

#Ending iteration with break statement when reached this iteration

i = 0

while (i<5):
 if (i ==2):
     break
 print('The value of i is : ', i)
 i = i + 1
else:
    print(' The value of i reached ', i)

'''
The value of i is :  0
The value of i is :  1
'''

#For Loops
x = ['apple', 'orange', 'banana']
for item in x:
    print(item)

'''
apple
orange
banana
'''

#For Loops for a string

for y in 'Orange':
    print(y)
'''
O
r
a
n
g
e
'''

#break statement

x = ['apple', 'orange', 'banana']
for item in x:
    if(item == 'orange'):
        break
    print(item)

'''
apple
'''

#Continue statement

x = ['apple', 'orange', 'banana']
for item in x:
    if(item == 'orange'):
        continue
    print(item)

'''
apple
banana
'''

for i in range(6):
    print(i)

'''
0
1
2
3
4
5
'''

for i in range(2,6):
    print(i)
'''
2
3
4
5
'''

for i in range(2,6, 2):
    print(i)
'''
2
4
'''

for i in range(6):
    print(i)
else:
    print('Completed looping till 5')

'''
0
1
2
3
4
5
Completed looping till 5
'''

#Nested for loop
adj = ['red', 'tasty','big']
fruit = ['apple', 'orange', 'banana']

for a in adj:
    for b in fruit:
        print(a,b)

'''
red apple
red orange
red banana
tasty apple
tasty orange
tasty banana
big apple
big orange
big banana
'''

#No content add pass to avoid error
for i in [0,1,2]:
    pass