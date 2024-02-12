class Student:
    def setName(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def setrollnum(self,rollnum):
        self.__rollnum=rollnum
    def getrollnum(self):
        return self.__rollnum

s1=Student()
s2=Student()
s1.setName("Mithilaw")
print(s1.getname())
s2.setName("Sastry")
print(s2.getname())
s1.setrollnum(2)
print(s1.getrollnum())