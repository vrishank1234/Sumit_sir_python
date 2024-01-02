# Write a Python program to create a class representing a shopping cart. Include
# methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name]['quantity'] += quantity
        else:
            self.items[item_name] = {'price': price, 'quantity': quantity}

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            if quantity >= self.items[item_name]['quantity']:
                del self.items[item_name]
            else:
                self.items[item_name]['quantity'] -= quantity
        else:
            print(f"{item_name} not found in the cart.")

    def calculate_total(self):
        total = 0
        for item_name, item_data in self.items.items():
            total += item_data['price'] * item_data['quantity']
        return total

    def display_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
        else:
            print("Shopping Cart:")
            for item_name, item_data in self.items.items():
                print(f"{item_name} - Rs.{item_data['price']} x {item_data['quantity']}")

# Example usage with user input:
cart = ShoppingCart()

while True:
    print("\n1. Add Item\n2. Remove Item\n3. Display Cart\n4. Calculate Total\n5. Exit")
    cho = input("Enter your choice (1/2/3/4/5): ")

    if cho == '1':
        item_name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity (default is 1): ") or 1)
        cart.add_item(item_name, price, quantity)
    elif cho == '2':
        item_name = input("Enter item name to remove: ")
        quantity = int(input("Enter quantity to remove (default is 1): ") or 1)
        cart.remove_item(item_name, quantity)
    elif cho == '3':
        cart.display_cart()
    elif cho == '4':
        print("Total Price:", cart.calculate_total())
    elif cho == '5':
        print("Thank you Visit Again!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
