# tuples are immutable (it will not be change)
# creating a tuple
t = ([1, 3, 6, 78, 345, 2,3,6,7,3])
t1 = ()  # empty tuple
t2 = ([1, ])  # tuple with single element

# print tuple
print(t)
print(t1)
print(t2)
print(t[0])

#methods in tuple

print('number of element present in tuple:',t.count(3))
print(t.index(345))
