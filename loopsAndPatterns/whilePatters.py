#draw various patters using while
#right angle triangle
'''num = int(input("Enter your number for pattern"))
i = 1
while i<=num:
    j = 1
    while j<=i:
        print("*",end=" ")
        j = j +1
    i = i+1
    print()'''

# pyramid
'''num = int(input("enter number: "))
i = 1
while i<=num:
    b = 1
    while b<=num-i:
        print(" ",end="")
        b=b+1
    j = 1
    while j<=i:
        print("*",end="")
        j = j+1
    i = i+1
    print()'''

#draw pyramid from *
'''k = 1
i = 1
while i<=5:
    b = 1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j = 1
    while j<=k:
        print("*",end="")
        j = j+1
    k = k+2
    print()
    i = i+1'''

# draw reverse pyramid
num = int(input("Emter the number: "))
i = 1
while (num > 0):
    b = 1
    while b<i:
        print(" ",end="")
        b = b+1
    j = 1
    while j<=(num*2)-1:
        print("*",end="")
        j = j+1
    print()
    num = num-1
    i = i+1






