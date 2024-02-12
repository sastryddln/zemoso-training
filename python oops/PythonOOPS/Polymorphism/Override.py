class Shape:
    st="Main class"

    def getName(self):
        return self.st

class xshape(Shape):
    def __init__(self,name):
        self.xsname=name
    def getName(self):
        print(super().getName()+","+self.xsname);
    
circle=xshape("Circle")
circle.getName()
