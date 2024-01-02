# Create a Bus child class that inherits from the Vehicle class. The default fare
# charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we
# need to add an extra 10% on full fare as a maintenance charge. So total fare for
# bus instance will become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare_charge(self):
        fare = self.capacity * 100
        return fare

class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)

    def fare_charge(self):
        fare = super().fare_charge()
        final_amount = fare + 0.1 * fare

        return final_amount

n=int(input("Seating capacity in Bus: "))
bus_obj = Bus(n)
fare = bus_obj.fare_charge()
print(f"The total fare for the bus is: Rs.{fare}")
