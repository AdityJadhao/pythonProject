num = int(input("Enter number: "))
i = 1
sum = 0
while (i <= num):
    if (i % 2 == 0):
        sum = sum + i
        i = i + 1
print("Sum is ", sum)
