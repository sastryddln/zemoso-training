class User:
    def __init__(self,u=None) -> None:
        self.__username=u
    def setUsername(self,x):
        self.__username=x
    def getUsername(self):
        return self.__username
    
Obj1=User("Sastry")
Obj2=User()
print(Obj1.getUsername())
print(Obj2.getUsername())
Obj2.setUsername("Mithilaw")
print(Obj2.getUsername())