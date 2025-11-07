#write class for bank account, 
#onwer, balance, 
#can deposit money, withdraw money

class BankAccount:
    rate = 0.02
    def __init__(self,_owner,_balance = 0):
        self.owner = _owner
        self.balance = _balance

    def get_owner(self):
        return self.owner
    def get_balance(self):
        return self.balance
    
    def set_owner(self,newowner):
        self.owner = newowner

    def deposit(self,amount):
        print(f'{self.owner}: Original balance: ${self.balance}')
        self.balance += amount
        print(f'{self.owner}: Amount deposited: ${amount}')
        print(f'{self.owner}: New balance: ${self.balance}')
    
    def withdraw(self,amount):
        if amount <= self.balance:
            print(f'{self.owner}: Original balance: ${self.balance}')
            self.balance -= amount
            print(f'{self.owner}: Amount withdrawn: ${amount}')
            print(f'{self.owner}: New balance: ${self.balance}')
        else:
            print(f'{self.owner}: insufficient funds. You have ${self.balance}.')
    
    def __add__(self,other):
        new_owner = f'{self.get_owner()} & {other.get_owner()}'
        new_balance = self.get_balance() + other.get_balance()
        new_account = BankAccount(new_owner,new_balance)
        return new_account
    
    def __str__(self):
        return f'Owner: {self.owner}, Balance: {self.balance}'
    
    def __eq__(self, other):
        return self.get_owner() == other.get_owner()
    
    def give_interest(self):
        self.balance = self.balance + (self.balance * self.rate)
       



nils_acc = BankAccount('Nils',200)
nils_acc.give_interest
print(nils_acc)
'''
nils_acc.deposit(100)
nils_acc.withdraw(200)
nils_acc.withdraw(200)

pibble_acc = BankAccount('Pibble',1000000)
pibble_acc.deposit(250000)

joint_acc = nils_acc + pibble_acc

joint_acc.deposit(100)

print(nils_acc == pibble_acc)
print(nils_acc == nils_acc)

new_acc = nils_acc

print(nils_acc == new_acc)
'''