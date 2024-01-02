# 14. To find the Euclidean distance between two points in a two dimensional space
# using class and object.

import math
class Euclidian:
    def __init__(self,a1,b1,a2,b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2

    def calculate(self):
        self.square = (((self.a2-self.a1)**2) + ((self.b2-self.b1)**2))
        self.distance = math.sqrt(self.square)
        return self.distance


def main():
    a1 = int(input("Enter point a1: "))
    b1 = int(input("Enter point b1: "))
    a2 = int(input("Enter point a2: "))
    b2 = int(input("Enter point b2: "))

    result = Euclidian(a1,b1,a2,b2)
    print(f"Euclidean distance between ({a1},{b1}) and ({a2},{b2}): {result.calculate()}")


if __name__=="__main__":
    main()