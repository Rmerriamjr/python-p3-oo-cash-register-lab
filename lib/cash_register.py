#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0, total=0):
    self.items = []
    self.discount = discount
    self.total = total
    self.last_trans = 0
  
  def add_item(self, title, price, quantity=1):
    sum = price * quantity
    self.total += sum
    for i in range(1, quantity + 1):
      self.items.append(title)
    
    self.last_trans = sum
    
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      percent_off = 1 - self.discount / 100
      self.total *= percent_off
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction(self):
    self.total -= self.last_trans
