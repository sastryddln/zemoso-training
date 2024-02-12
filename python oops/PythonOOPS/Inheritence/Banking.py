class Account:
    def __init__(self,title,balance):
        self.title=title
        self.balance=balance
    def getBalance(self):
        return self.balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    
    def withdrawl(self,amount):
        self.balance=self.balance-amount
class SavingAccounts(Account):
    def __init__(self,title,balance,interest):
        super().__init__(title,balance)
        self.interest=interest
    def interestrate(self):
        return ((self.interest)*(self.balance))/100
    
demo=SavingAccounts("Mithilaw",1000,10)
print(demo.interestrate())
demo.deposit(100)
print(demo.getBalance())

