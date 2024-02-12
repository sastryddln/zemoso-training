from abc import ABC,abstractmethod
class Animal:
    def __init__(self,name,sound):
        self.name=name
        self.sound=sound
    @abstractmethod
    def Animal_details(self):
        pass
class Dog(Animal):
    def __init__(self, name, sound,family):
        super().__init__(name,sound)
        self.family=family
    def Animal_details(self):
        print("name:",self.name)
        print("sound:",self.sound)
        print("family:",self.family)
class Sheep(Animal):
        def __init__(self,name,sound,color):
            super().__init__(name,sound)
            self.color=color
        def Animal_details(self):
            print("name:",self.name)
            print("sound:",self.sound)
            print("family:",self.color)
d= Dog("Bee", "Woof Woof", "Husky")
d.Animal_details()
print("")
s = Sheep("Bill", "Baa Baa", "White")
s.Animal_details()
