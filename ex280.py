#!/usr/bin/env python
# coding: utf-8

# In[6]:


import random


class Account:
    def __init__(self, name, balance):
        self.deposit_log = []
        self.withdraw_log = []
        
        self.balance = balance
        
    def deposit(self, amount):
        if amount>=1:
            self.deposit_log.append(amount)
            
    def withdraw (self, amount):
        if self.balance > amount:
            self.withdraw_log.append(amount)
            self.balance -= amount
            
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
#입금과 출금 사항을 기록하기 위해 deposit과 withdraw의 비어있는 리스트를 만들어준다.
#append함수를 이용하여 입금,출금 될 때마다 그 값을 리스트에 추가하도록 한다.

