
from datetime import datetime

class Bank:
 Bank_name="sbi"
 def __init__(self,accno,persname,balance):
        self.accno= accno
        self.balance= balance
        self.persname= persname
 def deposit(self,amount):
        self.balance+=amount
        print(Bank.Bank_name,"your account",self.accno,"has been credited with amt",amount,"on",datetime.today(),"ava_bal",self.balance)

 def withdrawl(self,amount):
        if self.balance > amount:
           self.balance-=amount
           print(Bank.Bank_name,"your account",self.accno,"has been debited with amt",amount,"on",datetime.today(),"avl_bal", self.balance)
        else:
            print("cancelled with error")

 def balance_enq(self,amount):
        print(self.balance)

obj=Bank(1001,"anu",5000)
obj.withdrawl(6000)
obj.deposit(1000)
obj.balance_enq(1001)
