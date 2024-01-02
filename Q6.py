# Define a class attribute “color” with a default value white. i.e., Every Vehicle
# should be white.

class Vehicle:
    color = "white"

    def __init__(self, model, year,color="white"):
        self.model = model
        self.year = year
        self.color = color

car1 = Vehicle(model="Tata Safari", year=2022)
car2 = Vehicle(model="Maruti Suzuki", year=2022)
car3 = Vehicle(model="Honda City", year=2023)

print(f"Car 1 - Model: {car1.model}, Year: {car1.year}, Color: {car1.color}")
print(f"Car 2 - Model: {car2.model}, Year: {car2.year}, Color: {car2.color}")
print(f"Car 3 - Model: {car3.model}, Year: {car3.year}, Color: {car3.color}")
