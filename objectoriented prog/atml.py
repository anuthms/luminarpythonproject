class Bank:
    def bal_enq(self):
        print("inside balance enq")

    def withdraw(self):
        print("inside withdraw")

    def __deposit(self):
        print("inside deposit")


class ATM(Bank):
    pass

#atm=ATM
#atm.withdraw()
#atm.bal_enq()
#atm.deposit()
obj=Bank()
obj._Bank__deposit()