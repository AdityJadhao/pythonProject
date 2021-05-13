i = int(input("Enter your num ber:"))
ori=i
sum =0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if(ori==sum):
    print("Number is armstrong number")
else:
    print("number is not armstrong")
