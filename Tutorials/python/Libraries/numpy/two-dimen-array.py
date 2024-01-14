import numpy as np

arr = np.array([[1,2],[3,4]])

print("The array elements: ", arr)
'''
The array elements: 
 [[1 2]
 [3 4]]
'''

print('First row first elm: ',arr[0][0])
#First row first elm:  1

print('Second row first elm: ',arr[1][0])
#Second row first elm:  3

print('The dimension is: ',arr.ndim)
#The dimension is:  2

print('The Size is :', arr.size)
#The Size is : 4

print('The shape is :', arr.shape)
#The shape is : (2, 2)