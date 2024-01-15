from cmath import log10
import numpy as np

#Generate 10 numbers between 1 and 3 and it will be floating pt numbers
a=np.linspace(1,3,10)
print(a)
#[1.         1.22222222 1.44444444 1.66666667 1.88888889 2.11111111
# 2.33333333 2.55555556 2.77777778 3.        ]

#Sum and axis
b=np.array([(1,2,3),(4,5,6)])
c=b.sum(axis=0)#column level
print(c)
#[5 7 9]

d=b.sum(axis=1)#Row level
print(d)
#[ 6 15]

#Square root
e=np.sqrt(b)
print(e)
#[[1.         1.41421356 1.73205081]
# [2.         2.23606798 2.44948974]]

#standard deviation
f=np.std(b)
print(f)
#1.707825127659933

#Straigten the array using ravel
g=np.ravel(b)
print(g)
#[1 2 3 4 5 6]

#Log base 10
h=np.log10(g)
print(h)
#[0.         0.30103    0.47712125 0.60205999 0.69897    0.77815125]

#Log base 10
i=np.log2(g)
print(i)
#[0.         1.         1.5849625  2.         2.32192809 2.5849625 ]