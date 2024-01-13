import numpy as np

a=['hello ']
b=['world']

c= np.char.add(a,b)
print('Concatinated array: ', c)

d = np.char.multiply(a, 3)
print('Multiplied array: ', d)

e = np.char.center(b, 20, fillchar='-')
print('Filled word: ', e)

