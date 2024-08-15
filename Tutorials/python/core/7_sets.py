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

