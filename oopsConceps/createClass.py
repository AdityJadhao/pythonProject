#creation of class

class myfirstClass():           #name should be start from camelcode and : is use after class name
    pass                        # pass is use to declare empty class , we can add body letter

ins_obj = myfirstClass()        # instance of class
print(ins_obj)                  # this gives class memery location

ins_obj1 = myfirstClass()       # create another class
print(ins_obj1)

# attributes in class
class myAttributeClass():
    str = "Hello class"             #class level attribute

attri = myAttributeClass()          #instance of class
print(attri.str)                    #print attribute of class
