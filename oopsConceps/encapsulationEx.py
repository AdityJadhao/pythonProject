#use get and set method

class enca():
    def setAge (self,num):
        self.age = num

    def getAge (self):
        return self.age

obj = enca()
obj.setAge(45)
print(obj.getAge())

