# Write a Python program to create a class representing a stack data structure.
# Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def size(self):
        return len(self.items)

elements = input("Enter elements for the stack: ").split(' ')

stack = Stack()
for element in elements:
    stack.push(element.strip())


while True:
    print("\n1. Push\n2. Pop\n3. Display Stack\n4. Exit")
    cho = input("Enter your choice (1/2/3/4): ")

    if cho == '1':
        element = input("Enter the element to push: ")
        stack.push(element)
    elif cho == '2':
        popped_element = stack.pop()
        if popped_element is not None:
            print("Popped element:", popped_element)
    elif cho == '3':
        print("Stack:", stack.items)
    elif cho == '4':
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
