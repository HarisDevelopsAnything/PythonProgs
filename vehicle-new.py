class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


class PetrolVehicle(Vehicle):
    def __init__(self, make, model, year, fuel_capacity):
        super().__init__(make, model, year)
        self.fuel_capacity = fuel_capacity

    def display_info(self):
        super().display_info()
        print(f"Fuel Capacity: {self.fuel_capacity}L")


class ElectricVehicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity}kWh")


class HybridVehicle(PetrolVehicle, ElectricVehicle):
    def __init__(self, make, model, year, fuel_capacity, battery_capacity):
        # Explicitly call the constructors of both parent classes
        PetrolVehicle.__init__(self, make, model, year, fuel_capacity=fuel_capacity)
        ElectricVehicle.__init__(self, make, model, year, battery_capacity=battery_capacity)

    def display_info(self):
        super().display_info()


# Example usage:
car1 = PetrolVehicle("Toyota", "Camry", 2022, 50)
car2 = ElectricVehicle("Tesla", "Model S", 2023, 100)
car3 = HybridVehicle("Toyota", "Prius", 2024, 30, 50)

print("Car 1:")
car1.display_info()
print("\nCar 2:")
car2.display_info()
print("\nCar 3:")
car3.display_info()
