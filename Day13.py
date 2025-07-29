#Day13:OOPS
#Q1:Create Account class with 2 attributes balance&Account no
#Create methods for debit,credit,&printing the balance

class Account:
    def __init__(self,account_no,balance):
        self.account_no=account_no
        self.balance=balance
    def debit(self,amount):
           self.balance-=amount
           print("Rs",amount,"Was debited")
           print("total balance=",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was credited")
        print("total balance=", self.get_balance())
    def get_balance(self):
        return self.balance
acc1=Account(5467,5000)
acc1.debit(1000)
acc1.credit(2000)