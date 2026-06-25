class BankAccount : 
    def __init__(self, balance : float = 0):
        self.__balance = balance #this is a private attributes

    def deposit(self, amount : float) :
        if amount > 0 :
            self.__balance += amount
            
    def get_balance(self) -> float:
        return self.__balance
    


account = BankAccount(1000)
account.deposit(200)

print(account.get_balance())