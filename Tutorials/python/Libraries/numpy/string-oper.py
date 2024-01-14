import numpy as np

a=['hello ']
b=['world']

c= np.char.add(a,b)
print('Concatinated array: ', c)
#Concatinated array:  ['hello world']

d = np.char.multiply(a, 3)
print('Multiplied array: ', d)
#Multiplied array:  ['hello hello hello ']

e = np.char.center(b, 20, fillchar='-')
print('Filled word: ', e)
#Filled word:  ['-------world--------']

f = np.char.capitalize(c)
print('Captalize :', f)
#Captalize : ['Hello world']

g = np.char.title(c)
print('Title Case is: ', g)
#Title Case is:  ['Hello World']

h=np.char.lower(c)
print('Lower Case is: ', h)
#Lower Case is:  ['hello world']

i=np.char.upper(c)
print('upper Case is: ', i)
#upper Case is:  ['HELLO WORLD']

j =np.char.split('Ocean is blue Mountain is tall')
print('Split Result is: ', j)
#Split Result is:  ['Ocean', 'is', 'blue', 'Mountain', 'is', 'tall']

k =np.char.splitlines('Ocean is blue \nMountain is tall')
print('Split Lines is: ', k)
#Split Lines is:  ['Ocean is blue ', 'Mountain is tall']

#Removes the leading and trailing char if it match
l =np.char.strip(['trunk','tree','boat'],'t')
print('Strip result is: ', l)
#Strip result is:  ['runk' 'ree' 'boa']

m =np.char.join([':','-'],['dmy','ymd'])
print('Join result is: ', m)
#Join result is:  ['d:m:y' 'y-m-d']

n =np.char.replace ('He is a good actor', 'good','great')
print('Replace result is: ', n)
#Replace result is:  He is a great actor