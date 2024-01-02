# Create a Python class called “Car” with attributes like make, model, and year.
# Then, create an object of the “Car” class and print its details.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car(make="BMW", model="M3", year=2022)


print("\n| Car Details |\n")
print(f" Make : {car.make}")
print(f" Model : {car.model}")
print(f" Year : {car.year}")
