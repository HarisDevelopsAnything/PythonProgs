class InvalidVectorError(Exception):
    def __init__(self):
        self.msg= "The vector has a zero component!"
class Vector:
    def __init__(self, a,b,c):
        self.a= a
        self.b= b
        self.c= c
    def showVector(self):
        print(f"{self.a}i+{self.b}j+{self.c}k")
    def __mul__(self, other):
        a= self.a*other.a
        b= self.b*other.b
        c= self.c*other.c
        return Vector(a,b,c)
    def __add__(self, other):
        a= self.a+other.a
        b= self.b+other.b
        c= self.c+other.c
        return Vector(a,b,c)
try:
    print("Vector 1: ")
    a1= int(input("Enter a: "))
    b1= int(input("Enter b: "))
    c1= int(input("Enter c: "))
    if(a1<0 or b1<0 or c1<0):
        raise InvalidVectorError
    print("Vector 2: ")
    a2= int(input("Enter a: "))
    b2= int(input("Enter b: "))
    c2= int(input("Enter c: "))
    if(a2<0 or b2<0 or c2<0):
        raise InvalidVectorError
    v1= Vector(a1,b1,c1)
    v2= Vector(a2,b2,c2)
    print("Vector 1: ")
    v1.showVector()
    print("Vector 2: ")
    v2.showVector()
    print(f"Sum of vectors:")
    (v1+v2).showVector()
    print(f"Product of vectors: ")
    (v1*v2).showVector()
except InvalidVectorError as ive:
    print(ive.msg)


    