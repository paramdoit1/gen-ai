import numpy as np

a = np.arange(5,46,5).reshape(3,3)
print(a)

'''
[[ 5 10 15]
 [20 25 30]
 [35 40 45]]
'''

#Iterating over array
for x in np.nditer(a):
   print(x)

'''
5
10
15
20
25
30
35
40
45
'''

#Iterating over array in c type
for x in np.nditer(a, order="C"):
    print(x)
'''
5
10
15
20
25
30
35
40
45
'''

#Iterating over array F Type
for x in np.nditer(a, order="F"):
    print(x)

'''
5
20
35
10
25
40
15
30
45
'''