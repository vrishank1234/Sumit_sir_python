# Create a base class called “Animal” and two subclasses, “Dog” and “Cat.” Add
# methods and attributes specific to each subclass. 

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "Woof!"

    def fetch(self):
        return f"{self.name} is fetching a ball."

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Meow!"

    def scratch(self):
        return f"{self.name} is scratching."

dog1 = Dog("Ozzi", 3, "Husky")
cat1 = Cat("Manii", 2, "Ragdoll")

print(dog1.name)      
print(dog1.speak())   
print(dog1.fetch()) 
print("\n")
print(cat1.name)      
print(cat1.speak())   
print(cat1.scratch()) 
