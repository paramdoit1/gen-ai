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
 print('The value of i is : ', i)
 i = i + 1
 if (i ==2):
     continue
else:
    print(' The value of i reached ', i)

'''
The value of i is :  0
The value of i is :  1
The value of i is :  3
The value of i is :  4
The value of i reached  5
'''