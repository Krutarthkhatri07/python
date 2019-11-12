class person:
    x=0
    def __init__(myobject,name,age):
        print('i am contructor')

    def fun(self):
        self.x=self.x+1
        print('so far',self.x)
    def __del__(self):
        print("i am destructed",self.x)
p1=person('krutarth','20')
p2=person('vidhi','24')
p1.fun()
p1.fun()
p2.fun()
print('end')