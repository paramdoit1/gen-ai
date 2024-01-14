import numpy as np

a = np.arange(9)
print(a)
#[0 1 2 3 4 5 6 7 8]

b =np.split(a,3)
print(b)
#[array([0, 1, 2]), array([3, 4, 5]), array([6, 7, 8])]

print(b[0])
#[0 1 2]

#Split based on given pattern.  first one till 4, 
# and second one till 7th postition, and rest in 3rd array
d = np.arange(10, 100,10)

c=np.split(d,[4,7])
print(c)
#[array([10, 20, 30, 40]), array([50, 60, 70]), array([80, 90])]