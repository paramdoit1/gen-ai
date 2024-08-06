#Strings are surrounded by single or double quotation marks in python.

#String declaration
a = 'sky is far, sea is blue'
b = "Hello World"
c = 'tree is "green"'
multiline = '''
               Rain rain go away
               Little Johny wants to play
               Rain rain go away
              ''' 
#String as arrays
print(a[0])
#s

for char in b:
    print(char)

'''
H
e
l
l
o

W
o
r
l
d
'''

#Getting string length
print(len(a))
#23

print('is' in a)
#True

if('rain' in multiline):
    print('Rain is present in multiline')
#Rain is present in multiline

if('tree' in multiline):
    print('Tree is present in multiline')
else:
    print('Tree is not present in multiline')
# Tree is not present in multiline

b = 'hello world'
print(b[2:6])
#llo
#starts with 0 and take string before 6

#Slice from start
print(b[:6])
#hello

#Methods
#Upper case
print(b.upper())
#HELLO WORLD

f = 'HELLO WORLD'
print(f.lower())
#hello world

g = ' Hello World! '
print(g.strip())
# Hello World!

print(f.replace('H', 'J'))
#JELLO WORLD

#Split methods
#The split() method returns a list where the text between the specified seperator becomes the list items

a = 'Hello, world!'
print(a.split(','))
#['Hello', 'world!']

#String concatenation

a= 'hello'
b = 'world'
c = a + ' '+b
print(c)
#hello world

#String formatting
price = 10
txt = f'The price of this product is {price} dollars'
print(txt)
#The price of this product is 10 dollars

price = 10
txt = f'The price of this product is {price:.2f} dollars'
print(txt)
#The price of this product is 10.00 dollars

#Escape Character
# An escape character is a backslash \ followed by the character that we need to insert

str = 'My Friend is in \'Phoenix\''
print(str)
#My Friend is in 'Phoenix'