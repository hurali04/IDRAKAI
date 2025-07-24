class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def show_balance(self):
        print("Name:", self.name)
        print("Balance:", self.balance)

name = input("Enter your name: ")
account = BankAccount(name)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Show Balance\n4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "3":
        account.show_balance()
    elif choice == "4":
        break
    else:
        print("Invalid option")
