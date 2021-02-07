class Bank:
    def bal_eq(self):
        print("inside balance enq")
    def withdraw(self):
        print("inside withdraw")
    def __deposit(self):   #private method/hide
        print("inside deposit")

class Atm(Bank):
    pass

b=Bank()
b.bal_eq()
b.withdraw()
#b.__deposit()  #private method does'nt acess outside the class but we can access outside using one method:-
b._Bank__deposit()
