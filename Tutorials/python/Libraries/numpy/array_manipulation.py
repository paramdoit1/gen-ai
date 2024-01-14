import numpy as np

a = np.arange(9)
print (a)
#[0 1 2 3 4 5 6 7 8]

#Reshape
b= a.reshape(3,3)
print (b)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''

#Flattens
c=b.flatten()
print(c)
#[0 1 2 3 4 5 6 7 8]

#Flatten by column
d=b.flatten(order="F")
print(d)
#[0 3 6 1 4 7 2 5 8]

# Transpose
e=b.transpose()
print(e)
'''
[[0 3 6]
 [1 4 7]
 [2 5 8]]
'''

#Three dimensional array
f= np.arange(8).reshape(2,2,2)
print(f)

'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''

