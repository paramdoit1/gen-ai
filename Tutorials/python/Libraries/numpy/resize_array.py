import numpy as np

a = np.array([[1,2,3],[4,5,6]])
print(a)
'''
[[1 2 3]
 [4 5 6]]
'''
print(a.shape)
#(2, 3)

b=np.resize(a,(3,2))
print(b)
'''
[[1 2]
 [3 4]
 [5 6]]
'''  

c=np.resize(a,(3,3))
print(c)
'''
[[1 2 3]
 [4 5 6]
 [1 2 3]]
'''  