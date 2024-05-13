class Bookings:
    def __init__(self, vehicle, passenger):
        self.vehicle= vehicle
        self.passenger= passenger
class Cab(Bookings):
    def __init__(self, name):
        self.name= name
class Passenger(Bookings):
    def __init__(self, name):
        
        self.name= name