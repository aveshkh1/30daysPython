#Day17:Mini Project
#Project Title: Bank Account Management System

from datetime import datetime

class BankAccount:
    def __init__(self, account_number, name, pin):
        self._balance = 0.0
        self.account_number = account_number
        self.name = name
        self._pin = pin
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transactions.append((datetime.now(), f"Deposited ${amount}"))
            print(f"${amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount, pin):
        if pin != self._pin:
            print("Invalid PIN.")
            return
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transactions.append((datetime.now(), f"Withdrew ${amount}"))
            print(f"${amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self, pin):
        if pin == self._pin:
            return self._balance
        else:
            print("Incorrect PIN.")
            return None
    def print_transactions(self):
        print(f"Transaction history for {self.name}:")
        for t in self.transactions:
            print(f"{t[0]} - {t[1]}")
class SavingsAccount(BankAccount):
    def __init__(self,account_number,name,pin,interest_rate=0.03):
        super().__init__(account_number,name,pin)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        interest=self._balance*self.interest_rate
        self._balance+=interest
        self.transactions.append((datetime.now(),f"Interest added ${interest:.2f}"))
        print(f"interest of ${interest:.2f}added")

class CurrentAccount(BankAccount):
    def __init__(self,name,account_number,pin,overdraft_limit=5000):
        super().__init__(name,account_number,pin)
        self.overdraft_limit=overdraft_limit
    def withdraw(self, amount, pin):
        if pin!=self._pin:
            print("Invalid pin")
            return
        if amount<=self._balance+self.overdraft_limit:
            self._balance-=amount
            self.transactions.append((datetime.now(),f"withdrew ${amount} with overdraft"))
            print(f"${amount} withdrawn using overdraft.")

        else:
            print("overdraft limit exceeded")

s1=SavingsAccount(123456,"Avesh",1111)
s1.deposit(10000)
s1.calculate_interest()
s1.withdraw(100,1111)
print(s1.get_balance(1111))

c1 = CurrentAccount("654321", "Karan", 2222)
c1.deposit(3000)
c1.withdraw(7500, 2222)
s1.print_transactions()