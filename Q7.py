# Implement a class inheritance as following.


class Vehicle:
    def vehicle_get(self):
        print("Vehicle class")

class Car(Vehicle):
    def car_get(self):
        print("Car class")

class Truck(Vehicle):
    def truck_get(self):
        print("Truck class")

class Bike(Vehicle):
    def bike_get(self):
        print("Bike class")


car = Vehicle()
car = Bike()

car.vehicle_get()
car.bike_get()