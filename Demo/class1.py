class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fun(self):
        print(self.name)
    def __del__(self):
        print("i am destructed")
p1=person('krutarth','39')
p1.age=40
####### del p1 ########## use for delete the object of class
####### del p1.age ##### use for delete the properties of object
print(p1.name)
print(p1.age)
p1.fun()