#craete account,deposit,withdrawal,balance

from datetime import datetime

class Bank:

    bank_name="sbi"
    def create_account(self,accno,person_name,min_balance):
        self.accno=accno
        self.person_name=person_name
        self.balance=min_balance


    def deposit(self,amount):
        self.balance+=amount
        print(Bank.bank_name,"your account",self.accno,"has been credited with amt",amount,"on",datetime.today(),"amt balance",self.balance)

    def withdrawal(self,amount):

         if self.balance>amount:
             self.balance-=amount
             print(Bank.bank_name,"your account",self.accno,"has been debited with amt",amount,"on",datetime.today(),"amt balance",self.balance)
         else:
             print("transaction cancelled with error code")

    def balance_enq(self):
        print(self.balance)

obj=Bank()
obj.create_account(9999,"niya",4000)
obj.deposit(6000)

obj=Bank()
obj.create_account(9999,"ani",5000)
obj.withdrawal(1000)


#different types of variables
#1)instance variable
#2)static variable or class variable(same argument first initialize then access with class name)

#using constructor

from datetime import datetime

class Bank:

    bank_name="sbi"
    def __init__(self,accno,person_name,min_balance):
        self.accno=accno
        self.person_name=person_name
        self.balance=min_balance


    def deposit(self,amount):
        self.balance+=amount
        print(Bank.bank_name,"your account",self.accno,"has been credited with amt",amount,"on",datetime.today(),"amt balance",self.balance)

    def withdrawal(self,amount):

         if self.balance>amount:
             self.balance-=amount
             print(Bank.bank_name,"your account",self.accno,"has been debited with amt",amount,"on",datetime.today(),"amt balance",self.balance)
         else:
             print("transaction cancelled with error code")

    def balance_enq(self):
        print(self.balance)

obj=Bank(9999,"niya",4000)
obj.deposit(6000)

obj=Bank(9999,"ani",5000)
obj.withdrawal(1000)