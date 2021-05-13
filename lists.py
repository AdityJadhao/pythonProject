# create list
l1 = [1, 'Aditya', 3.21, True]
print(l1)

#always use [] for creating list and work with list
print(l1[0:2])

# update list
l1[0] = 98
print(l1)

# access using index
print(l1[1])

# slicing of list
friends =['Amra','Sharma','pappya','manya']
print(friends)
print(friends[0:3])
print(friends[-2:])

#list methods
l2 = [1, 3, 6,45,2,78,900,4]
print(l2.count(3))
# print(l2.sort())     #wrong way
l2.sort()
print(l2)
l2.reverse()
print(l2)
l2.append(786)    #always add at the end of list
print(l2)
l2.insert(0,222)
print(l2)
l2.insert(3,1)
print(l2)
l2.pop(1)  #remove from index
print(l2)
l2.remove(45)  #remove actual value in the list
print(l2)
