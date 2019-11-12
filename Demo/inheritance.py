class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self):
        print(self.name)
        print(self.age)
class student(person):
    def __init__(self,mark):
        super().__init__('krutarth','20')
        self.mark=mark
    def fun1(self):
        print(self.mark)
p1=student('100')
p1.fun()
p1.fun1()