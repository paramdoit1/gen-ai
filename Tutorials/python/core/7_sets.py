# Sets are used to store multiple items in a single variable
# Items in set are unordered,unchangeable, and do not allow duplicate values
# Unordered means that items in set do not have a defined order.
# Set items can appear in a different order every time when it is used and cannot be referrenced by index or key.
# The values True and 1 are considered the same value in sets and are treated as duplicates
# Once a set is created , we cannot change its items but we can add new items.

s1 = {'pineapple', 'apple', 'cherry'}
print(s1)

#Looping through the set

for item in s1:
    print(item)
'''
apple
cherry
pineapple
'''

print("cherry" in s1)
#True

#Add Set items
# Once set is created, we cannot change items but we can add new onces
# use add() for adding items in the method

s1.add('grapes')
print(s1)
#{'apple', 'cherry', 'grapes', 'pineapple'}

#update the set to add another set. It can be list, set or tuples
s2 = {'plum'}
s1.update(s2)
print(s1)
#{'plum', 'grapes', 'apple', 'cherry', 'pineapple'}

#Removing items in the set
s1.remove('pineapple')
print(s1)
#{'plum', 'grapes', 'apple', 'cherry'}

#Remove will throw error if item does not exists but discard will not throw error.
s1.discard('cherry')
print(s1)
#{'plum', 'grapes', 'apple'}

#Removing the random item from the set and return it
s1.pop()
print(s1)
#{'grapes', 'apple'}

#Clear method clears the elements of the set
s1.clear()
print(s1)
set()

#del is used to delete the set
del s1
#print (s1)
#NameError: name 's1' is not defined

#Union() and update() methods join all items from both sets
#intersection() keeps only the duplicates
#difference() keeps the items from the first set not in the other set
#Symmetic difference() keeps all items in both except the duplicates

set1 = {1, 2, 3}
set2 = {"a", "b", "c", 3}
set3 = set1.union(set2)
print('Union Results', set3)
#Union Results {1, 2, 3, 'a', 'c', 'b'}

set4 = {'apple', 'orange'}
set5 = set1.union(set2, set4)
print('Multiple set Union Results', set5)
#Multiple set Union Results {1, 2, 3, 'a', 'c', 'apple', 'orange', 'b'}

#Union using |
set6 = set1 | set2 | set4
print('Multiple set Union Results using | ', set6)
#Multiple set Union Results using |  {1, 2, 3, 'a', 'c', 'apple', 'orange', 'b'}

#Updating set
set1.update(set2)
print('Set after update: ',set1)
#Set after update:  {1, 2, 3, 'a', 'c', 'b'}

#Intersection keep only the duplicates. The intersection() method returns new set
#that are present in both sets.

set3 = set1.intersection(set2)
print('Intersection results',set3)
#Intersection results {'a', 3, 'c', 'b'}

#difference() method return a new set that contain items in first set that are not present in second.
set3 = set1 -set2
print('difference results',set3)
#difference results {1, 2}

#diffence using difference method
set3 = set1.difference(set2)
print('difference results using difference',set3)
#difference results using difference {1, 2}

#Symmetic difference() keeps all items in both except the duplicates

set3 = set1.symmetric_difference(set2)
print('difference results using Sys difference',set3)
#difference results using Sys difference {1, 2}