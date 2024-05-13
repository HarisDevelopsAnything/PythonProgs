class Vehicle:
    def __init__(self, vid, vname, owner, regno, color):
        self.vid= vid
        self.vname= vname
        self.owner= owner
        self.regno= regno
        self.color= color
    def displayData(self):
        print("+"*25)
        print(f"Vehicle ID: {self.vid}")
        print(f"Vehicle Name: {self.vname}")
        print(f"Owner of vehicle: {self.owner}")
        print(f"Reg. No.: {self.regno}")
        print(f"Color: {self.color}")
        print("-"*25)
class PetrolVehicle(Vehicle):
    def __init__(self, vid, vname, owner, regno, color, fcap, cyl, hp, maxrange):
        super().__init__(vid, vname, owner, regno, color)
        self.fcap= fcap
        self.cyl= cyl
        self.hp= hp
        self.maxrange= maxrange
    def displayData(self):
        Vehicle.displayData(self)
        print(f"Fuel capacity: {self.fcap} L")
        print(f"Cylinders: {self.cyl} CYL")
        print(f"Horsepower: {self.hp} HP")
    def calcMileage(self):
        mileage= self.fcap/self.maxrange
        return mileage
class ElectricVehicle(Vehicle):
    def __init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange):
        super().__init__(vid, vname, owner, regno, color)
        self.batterycap= batterycap
        self.chargespd= chargespd
        self.maxrange= maxrange
    def displayData(self):
        print(f"Battery capacity: {self.batterycap} kWh")
        print(f"Charging speed: {self.chargespd}kW")
    def calcMileage(self):
        mileage= self.batterycap/self.maxrange
        return mileage
class HybridVehicle(PetrolVehicle, ElectricVehicle):
    def __init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp):
        PetrolVehicle.__init__(self, vid, vname, owner, regno, color, fcap, cyl, hp, maxrange)
        ElectricVehicle.__init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange)
        
    def displayData(self):
        PetrolVehicle.displayData(self)
        ElectricVehicle.displayData(self)
class Car(HybridVehicle):
    def __init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp, trunk_space):
        super().__init__(vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp)
        self.trunk_space = trunk_space
        
    def displayData(self):
        HybridVehicle.displayData(self)
        print(f"Trunk Space: {self.trunk_space} cubic feet")
        
class Bike(HybridVehicle):
    def __init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp, top_speed):
        super().__init__(vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp)
        self.top_speed = top_speed
    def displayData(self):
        HybridVehicle.displayData(self)
        print(f"Top Speed: {self.top_speed} mph")
class Truck(PetrolVehicle):
    def __init__(self, vid, vname, owner, regno, color, fcap, cyl, hp, maxrange, cargo_capacity):
        super().__init__(vid, vname, owner, regno, color, fcap, cyl, hp, maxrange)
        self.cargo_capacity = cargo_capacity
    def displayData(self):
        PetrolVehicle.displayData(self)
        print(f"Cargo Capacity: {self.cargo_capacity} cubic feet")
vid= input("Vehicle ID: ")
vname= input("Vehicle name: ")
owner= input("Owner's name: ")
regno= input("Reg. no.: ")
color= input("Vehicle color: ")
print("1) Car\n2) Bike\n3) Truck")
ch= int(input("Enter your choice: ")[0])
if ch==1:
    batterycap= int(input("Battery capacity: "))
    chargespd= int(input("Charging speed: "))
    maxrange= int(input("Max range: "))
    fcap= int(input("Fuel capacity: "))
    cyl= int(input("No. of cyinders: "))
    hp= int(input("HP: "))
    trunk_space= int(input("Trunk space: "))
    vehicle= Car(vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp, trunk_space)
elif ch==2:
    batterycap= int(input("Battery capacity: "))
    chargespd= int(input("Charging speed: "))
    maxrange= int(input("Max range: "))
    fcap= int(input("Fuel capacity: "))
    cyl= int(input("No. of cyinders: "))
    hp= int(input("HP: "))
    top_speed= int(input("Top speed: "))
    vehicle= Bike(vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp, top_speed)
elif ch==3:
    fcap= int(input("Fuel capacity: "))
    cyl= int(input("No. of cyinders: "))
    hp= int(input("HP: "))
    maxrange= int(input("Max range: "))
    cargo_capacity= int(input("Cargo capacity: "))
    vehicle= Truck(vid, vname, owner, regno, color, fcap, cyl, hp, maxrange, cargo_capacity)
Tesla= Car("1", "Etios", "Haris", "23bcs104", "Navy Blue", 4500, 45, 450, 50, 4, 1250, 2000)
Tesla.displayData()
Ather= Bike("2", "Ather 450X", "Jonathan", "23bcs105", "Space Grey", 3400, 37, 150, 10, 2, 250, 150)
Ather.displayData()
Cybertruck= Truck("3", "Tesla Cybertruck", "Malesh", "23bcs106", "Sierra", 3400, 6, 2450, 600, 10000)
Cybertruck.displayData()