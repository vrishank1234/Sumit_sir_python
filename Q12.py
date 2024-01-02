# 12. Define a class with a generator which can iterate the numbers, which are divisible
# by 7, between a given range 0 and n.


class Generator:
    def iterate(self, number):
        return [i for i in range(number + 1) if i % 7 == 0]

def main():
    gen = Generator()
    print("Divisibility by 7 checker")
    num = int(input("Enter limit: "))
    print(gen.iterate(num))

if __name__ == "__main__":
    main()
