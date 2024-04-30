class Vehicle:
    def __init__(self, vid, vname, owner, regno, color):
        self.vid = vid
        self.vname = vname
        self.owner = owner
        self.regno = regno
        self.color = color

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
        self.fcap = fcap
        self.cyl = cyl
        self.hp = hp
        self.maxrange = maxrange

    def displayData(self):
        super().displayData()
        print(f"Fuel capacity: {self.fcap} L")
        print(f"Cylinders: {self.cyl} CYL")
        print(f"Horsepower: {self.hp} HP")

    def calcMileage(self):
        mileage = self.fcap / self.maxrange
        return mileage


class ElectricVehicle(Vehicle):
    def __init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange):
        super().__init__(vid, vname, owner, regno, color)
        self.batterycap = batterycap
        self.chargespd = chargespd
        self.maxrange = maxrange

    def displayData(self):
        super().displayData()
        print(f"Battery capacity: {self.batterycap} kWh")
        print(f"Charging speed: {self.chargespd} kW")

    def calcMileage(self):
        mileage = self.batterycap / self.maxrange
        return mileage


class HybridVehicle(PetrolVehicle, ElectricVehicle):
    def __init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange, fcap, cyl, hp):
        # Call ElectricVehicle's __init__ first
        ElectricVehicle.__init__(self, vid, vname, owner, regno, color, batterycap, chargespd, maxrange)
        # Call PetrolVehicle's __init__ with remaining arguments
        PetrolVehicle.__init__(self, vid, vname, owner, regno, color, fcap, cyl, hp, maxrange)



    def displayData(self):
        super().displayData()
        print("Hybrid Vehicle Information:")
        print("Petrol Vehicle Information:")
        print(f"Fuel capacity: {self.fcap} L")
        print(f"Cylinders: {self.cyl} CYL")
        print(f"Horsepower: {self.hp} HP")
        print("Electric Vehicle Information:")
        print(f"Battery capacity: {self.batterycap} kWh")
        print(f"Charging speed: {self.chargespd} kW")


class Car(HybridVehicle):
    pass


class Bike(HybridVehicle):
    pass


class Truck(PetrolVehicle):
    pass


Etios = PetrolVehicle("E30", "Toyota Etios", "Haris", "23bcs2020", "Grey", 400, 4, 1250, 250)
Etios.displayData()

Hycross = HybridVehicle("F20", "Toyota Hycross", "Haris", "23bcs101", "White", 4500, 45, 250, 45, 4, 2250)
Hycross.displayData()
