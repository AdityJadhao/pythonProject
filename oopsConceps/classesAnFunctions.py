class mySecondClass():
    def firstFuc(self):
        print("Hello function")
        #print(self)

    def secondCls(self,age):
        print("Hello Secondclass")
        print(f"your age is {age}")

    def thirdCls(self,name,age,address,height):
        print("Hello class three")
        print(f"your name is {name} and age is {age} and height is {height}")

obj = mySecondClass()
obj.firstFuc()
obj.secondCls(25)
obj.thirdCls("Amra",29,"pune",5.9)


