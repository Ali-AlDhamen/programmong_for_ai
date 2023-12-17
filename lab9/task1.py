# Task 1
# Write a program that stores the information of a Bank Account (Account class) and then it allows the user to deposit, withdraw and display balance. The class should include the following variables:  
# •	name 
# •	balance (private)
# Use the following guidelines:
# •	In Account class: 
# o	 Add a constructor. 
# o	Add getters for private variables.
# o	Create function deposit that receives amount and update the balance after deposit.
# o	Create function withdraw that receives amount and update the balance after withdrawing.
# o	Add a Destructor. 
# •	Ask the User for input:
# o	Enter name and id ,then create an object
# o	Choose the Option:
# 	1 - deposit
# 	2 - withdraw
# 	3 – Display balance
# 	4 - Exit
# •	Perform the Operation
# •	Repeat until Option 4 is chosen
# •	After the user exit menu , add VIP attribute if balance is greater than 10,000 and print the account information.
# •	Destroy the object


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

    def __del__(self):
        print("Account deleted")
        
    def __str__(self):
        res = f"Name: {self.name}\n"
        res += f"Balance: {self.__balance}"
        if hasattr(self, 'vip'):
            res += "\nVIP"
        return res


name = input("Enter name: ")
balance = int(input("Enter balance: "))
account = Account(name, balance)


def menu():
    print("1 - deposit\n2 - withdraw\n3 – Display balance\n4 - Exit")
    return int(input("Choose option: "))
while True:
    option = menu()
    
    match option:
        case 1:
            amount = int(input("Enter amount: "))
            account.deposit(amount)
        case 2:
            amount = int(input("Enter amount: "))
            account.withdraw(amount)
        case 3:
            print(account.get_balance())
        case 4:
            break
        case _:
            print("Invalid option")
            
if account.get_balance() > 10000:
    account.vip = True

print(account)

    
del account