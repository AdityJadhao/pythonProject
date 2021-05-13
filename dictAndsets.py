#dictonary is collection of key value pair

#create dictionary
myDic = {
    "Power": "Knowledge",
    "Aditya": "Student",
    "Marks": [1,2,3,5],
    "myDic2": {'Taste': 'Sweet'}    #nested dictionary

}

print(myDic['Power'])
print(myDic['myDic2']['Taste'])
print(myDic.keys())
print(myDic.values())
print(myDic.items())

#update dictionary
updateDic = {
    "keys" : "values"
}
myDic.update(updateDic)
print(myDic)
print(type(myDic))

print(myDic.get('Power')) # use this, if value is not present , it return NOne
print(myDic['Power']) # if value is not present , it return key error