#!/usr/bin/env python3

class CashRegister:
  # total = 0
  # items = []
  # last_item = []
  
  def __init__(self, discount=0):
    self.discount = discount

    self.total = 0
    self.items = []
    self.last_item = []
  
  def add_item(self, title, price, quantity=1):
    self.total = self.total + price * quantity
    for each in range(quantity):
      self.items.append(title)
    self.last_item = [title, price, quantity]

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = self.total - self.total * (self.discount / 100)
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total = self.total - self.last_item[1] * self.last_item[2]
