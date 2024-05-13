class Animal:
    def __init__(self, name):
        self.name= name
    def move(self):
        print(f"Animal {self.name} moves.")
    def eat(self):
        print(f"Animal {self.name} eats.")
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)
    def move(self):
        print(f"Mammal {self.name} moves.")
    def eat(self):
        print(f"Mammal {self.name} eats.")
class Reptile(Animal):
    def __init__(self, name):
        super().__init__(name)
    def move(self):
        print(f"Reptile {self.name} moves.")
    def eat(self):
        print(f"Reptile {self.name} eats.")
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    def move(self):
        print(f"Bird {self.name} moves.")
    def eat(self):
        print(f"Bird {self.name} eats.")
def MRO(cls):
    print(f"MRO of class {cls.__name__}:")
    for i in cls.mro():
        print(i.__name__, end=" ")
        if i.__name__!="object":
            print("=>",end=" ")
    print()
print("For Animal class: ")
animal= Animal("Goat")
animal.move()
animal.eat()
MRO(Animal)
print("For Mammal class: ")
mammal= Mammal("Human")
mammal.move()
mammal.eat()
MRO(Mammal)
print("For Reptile class: ")
reptile= Reptile("Lizard")
reptile.move()
reptile.eat()
MRO(Reptile)
print("For Bird class: ")
bird= Bird("Sparrow")
bird.move()
bird.eat()
MRO(Bird)
print()
