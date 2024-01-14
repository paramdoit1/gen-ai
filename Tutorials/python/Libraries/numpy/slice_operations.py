import numpy as np

a = np.arange(10)
print(a)
#[0 1 2 3 4 5 6 7 8 9]

b=a[3:]
print(b)
#[3 4 5 6 7 8 9]

c=a[:3]
print(c)
#[0 1 2]

print(a[3])
#2

#Start, end,step and get the numbers
d=slice(2,9,2)
print(a[d])
#[2 4 6 8]