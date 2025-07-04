"""
Operations in a List
"""

# 1. Creating a list
list = [1,2,3,4,5]

# 2. Appending
list.append(7)
# print(list)

# 3. inserting
list.insert(5, 6)
# print(list)

# 4. delete
list.remove(3)
# print(list)

del list[2]
# print(list)

# 5. sorting the list
list2 = [1,2,9,4,3]
list2.sort()
# print(list2)

# 6. reverse sort
list2.sort(reverse = True)
# print(list2)

# 7. Slicing in lists
num = [1,2,3,4,5,6,7,8,9,10]
sublist = num[4:7]
print(sublist)

