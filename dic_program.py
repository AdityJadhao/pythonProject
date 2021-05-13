# write a program to display dictionary for user and conver from hindi to english

'''newDic = {
    "Pankha" : 'Fan',
    'Vastu' : 'Item',
    'Mitra' : 'Friends',
}

print("Select your word: ",newDic.keys())
a = input("Enter Here: ")
print("English translation of your word is :",newDic.get(a)) #if we use get , will not get key error if word is not present'''

# take 4 numbers from user and  display unique word
'''num1 = int(input("Enter number 1: \n"))
num2 = int(input("Enter number 2: \n"))
num3 = int(input("Enter number 3: \n"))
num4 = int(input("Enter number 4: \n"))

Mynumbers = {num1,num2,num3,num4}
print('Unique numbers are:',Mynumbers)'''

# Enter values from friends and display their fav subjects
favlang = {}   #create empty dic
f1 = input("Enter value from Amol\n")      # enter values from user
f2 = input("Enter value from Aniket\n")
f3 = input("Enter value from Aditya\n")
f4 = input("Enter value from Astha\n")
# add that values in dic
favlang ['Amol'] = f1
favlang ['Aniket'] = f2
favlang ['Aditya'] = f3
favlang ['Astha'] = f4

#print dic
print("Favrt languages of friends are ",favlang)
