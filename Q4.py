# Write a Python program to create a class representing a bank. Include methods for
# managing customer accounts and transactions.

class Bank:
    def __init__(self):
        self.balance = 750000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited Rs.{amount}.\nNew balance: Rs.{self.balance}")
        else:
            print("Invalid amount, Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"\nWithdrew Rs.{amount}.\nNew balance: Rs.{self.balance}")
        else:
            print("Invalid amount for withdrawal or insufficient funds.")

    def check_balance(self):
        print(f"Current balance: Rs.{self.balance}")


bank = Bank()

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        bank.check_balance()
    elif choice == '2':
        amount = float(input("Enter the deposit amount: "))
        bank.deposit(amount)
    elif choice == '3':
        amount = float(input("Enter the withdrawal amount: "))
        bank.withdraw(amount)
    elif choice == '4':
        print("Thank you for using our banking system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
