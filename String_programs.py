# name = input ("Enter your Name:\n")
# print("Good Morning: " + name)

# write a program to take input date and name and replace in letter
letter = '''Dear <|Name|>
You are awesome.\nkeep faith in god and practice.
Thank you,\n<|Name2|>
Date : <|Date|>
'''
'''X = input("Enter your Name: ")
Dt = input("Enter date in mm\dd\yyy:")
letter = letter.replace('<|Name|>', X)
letter = letter.replace('<|Date|>', Dt)
letter = letter.replace('<|Name2|>', 'God')
print(letter)'''

# detect find double spaces in string
st = "This is sample string  and it has    doublespace"
doublespace = st.find("  ")
print(doublespace)
st = st.replace("  ", " ")
print(st)
