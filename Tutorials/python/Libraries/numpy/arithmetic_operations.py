import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
   
b=np.array([10,20,30])

#addition
c=np.add(a,b)
print(c)
'''
[[10 21 32]
 [13 24 35]
 [16 27 38]]
'''

#Subtraction
d=np.subtract(a,b)
print(d)
'''
[[-10 -19 -28]
 [ -7 -16 -25]
 [ -4 -13 -22]]
'''

#Multiplication
e=np.multiply(a,b)
print(e)

'''
[[  0  20  60]
 [ 30  80 150]
 [ 60 140 240]]
'''

#division
f=np.divide(a,b)
print(f)

'''
[[0.         0.05       0.06666667]
 [0.3        0.2        0.16666667]
 [0.6        0.35       0.26666667]]
'''
