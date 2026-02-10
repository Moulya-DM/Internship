# Task-1: Polymorphism – Payment System
# Problem Statement
# Create a program for a Payment System using method overriding.
# Requirements
# Create a parent class Payment
# method: pay()
# Create child class GooglePay (inherits Payment)
# override pay()
# Create child class PhonePe (inherits Payment)
# override pay()
# Create child class CreditCard (inherits Payment)
# override pay()
# Create one object for each class and call pay() method.


# Parent class
class Payment:
    def pay(self):
        print("Processing payment using generic payment method.")


# Child class: GooglePay
class GooglePay(Payment):
    def pay(self):
        print("Processing payment using Google Pay.")


# Child class: PhonePe
class PhonePe(Payment):
    def pay(self):
        print("Processing payment using PhonePe.")


# Child class: CreditCard
class CreditCard(Payment):
    def pay(self):
        print("Processing payment using Credit Card.")


# Testing Method Overriding

payment = Payment()
google_pay = GooglePay()
phonepe = PhonePe()
credit_card = CreditCard()

print("---- Payment System ----")
payment.pay()
google_pay.pay()
phonepe.pay()
credit_card.pay()
