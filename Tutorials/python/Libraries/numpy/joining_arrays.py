import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

c=np.concatenate((a,b))
print(c)

'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

d=np.concatenate((a,b), axis=1)
print(d)

'''
[[1 2 5 6]
 [3 4 7 8]]
'''

