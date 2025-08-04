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
