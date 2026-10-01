# Validation in Methods
# Create a class called BankAccount with: 1.owner, and 2.balance, which defaults to 0
# Add these methods:
# 1. deposit(amount)
# * Add amount to the balance.
# * Raise a ValueError if amount <= 0.
# 2. withdraw(amount)
# * Subtract amount from the balance.
# * Raise a ValueError if amount is greater than the current balance.

class BankAccount:
  def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("The amount should be higher than 0.")
    else:
      self.balance += amount

  def withdraw(self, amount):
    if amount > self.balance:
      raise ValueError("The amount can't be higher than the balance.")
    else:
      self.balance -= amount

my_account = BankAccount("Yas")

my_account.deposit(50)
print(my_account.balance)

my_account.withdraw(30)
print(my_account.balance)

