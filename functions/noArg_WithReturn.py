# write a program to find avg of 3 numbers with return arguments using function

def average() :
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    avg = ((a + b + c) / 3)
    return avg


x = average()
print(x)
