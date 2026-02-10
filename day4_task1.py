# Task-1: Hierarchical Inheritance 
# Problem Statement
# Create a program for a Bank System using Hierarchical Inheritance.
# Requirements
# Create a parent class BankAccount
# Attributes:
# account_holder
# balance
# Methods:
# deposit(amount)
# withdraw(amount)
# display_balance()
# Create a child class SavingsAccount that inherits from BankAccount
# Attribute:
# interest_rate
# Method:
# add_interest()
# Create another child class CurrentAccount that inherits from BankAccount
# Attribute:
# overdraft_limit
# Method:
# withdraw_with_overdraft(amount)
# Create one object of SavingsAccount and one object of CurrentAccount and test all methods.


class BankAccount:
    def __init__(self, account_holder):
        self.account_holder=account_holder
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount


    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.display_balance()
        else:
            print("You have insufficient amount in your Account.")


    def display_balance(self):
        print("The balance is",self.balance)




class SavingsAccount(BankAccount):
    def __init__(self,interest_rate,name):
        temp_interest=interest_rate/100
        self.interest_rate=temp_interest
        super().__init__(name)
    def add_interest(self):
        self.balance*=(1+self.interest_rate)
        super().display_balance()




class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit, name):
        self.overdraft_limit=overdraft_limit
        super().__init__(name)
    def withdraw_with_overdraft(self,amount):
        if amount<self.balance+self.overdraft_limit:  # 590 < 600
            self.balance-=amount
            super().display_balance()
        else:
            print("Overdraft limit is exceeded")


SA=SavingsAccount(10,"Raja")
CA=CurrentAccount(100,"Raja")


SA.deposit(100)
SA.withdraw(30)
SA.add_interest()


CA.deposit(500)
CA.withdraw_with_overdraft(590)
