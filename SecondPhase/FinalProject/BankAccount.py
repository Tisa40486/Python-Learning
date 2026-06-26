import json
from datetime import datetime
import os
        
folderName = "SecondPhase/FinalProject/BankData"
jsonFile = f"{folderName}/Accounts.json"
command = 0
accounts=[]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if not os.path.exists(folderName):
    os.makedirs(folderName)
    
if not os.path.exists(jsonFile) or os.path.getsize(jsonFile) == 0:
    with open(jsonFile, "w") as f:
        json.dump([], f) 
        
        
CLI = {
    "Create Account" : 1,
    "Deposit" : 2,
    "Withdraw" : 3,
    "Check Balance" : 4,
    "Transfert" : 5,
    "List Accounts" : 6,
    "Quit" : 7
}

class Account : 
    def __init__(self, account_holder:str, balance : float = 0):
        self.name = account_holder
        self.__balance = balance
    
    def deposit(self, amount: float):
        self .__balance += amount
        
    def withdraw(self, amount: float):
        self .__balance -= amount
        
    def get_balance(self):
        return f"{self.__balance}"
    
    def tranfer(self, other_account: Account, amount: float):
        self.withdraw(amount)
        other_account.deposit(amount)
    
    def to_dict(self):
        return {
            "name": self.name,
            "balance": self.__balance
        }
    
    @staticmethod
    def from_dict(data):
        return Account(data["name"], data["balance"])
        
class Bank :
    def __init__(self):
        with open(f"{jsonFile}", "r") as file:
            loaded = json.load(file)
            self.accounts = [Account.from_dict(data) for data in loaded]


    def create_Account(self, accountName:str, amount: int = 0):
        self.accounts.append(Account(accountName, amount))
        accounts_data = accounts
        with open(f"{jsonFile}", "w") as file:
            json.dump(accounts_data, file)
            
    def find_Account(self, accountName:str):
        for account in self.accounts:
            if account.name == accountName:
                return account
        writeLog(f"\"{accountName}\" not found")
        
    def list_Account(self):
        for account in self.accounts:
            print(f"{account.name} : {account.get_balance()}€")
            
    def save_to_file(self):
        accounts_data = [acc.to_dict() for acc in self.accounts]
        with open(f"{jsonFile}", "w") as file:
            json.dump(accounts_data, file)
            
            
def writeLog(message : str) :
    dt = datetime.now()
    
    with open(f"{folderName}/log.txt", "a") as file:
        file.write(f"New log entry : {dt} \n")
        file.write(f" --{message} \n")
 
        
bank = Bank()

print("DONT FORGET TO QUIT(7) TO SAVED")
while command != CLI["Quit"]: 
    try: 
        for action, number in CLI.items():
            print(f"{number}. {action}")
        
        command = input("Choose an option : ")
        command = int(command)
        
        if command == CLI["Create Account"]:
            accountName = input("Enter the account name : ")
            bank.create_Account(accountName)
            writeLog(f"Account Create with the name of \"{accountName}\"")
        
        if command == CLI["Deposit"]:
            account = input("Enter your account name : ")
            amount = input("Enter the amount : ")
            amount = int(amount)
            bankAcccount = bank.find_Account(account) 
            bankAcccount.deposit(amount) 
            writeLog(f"Amount of {amount} deposed on {bankAcccount.name}'s account.")
           
        if command == CLI["Withdraw"]:
            account = input("Enter your account name : ")
            amount = input("Enter the amount : ")
            amount = int(amount)
            bankAcccount = bank.find_Account(account) 
            bankAcccount.withdraw(amount) 
            writeLog(f"Amount of {amount} withdrawed on {bankAcccount.name}'s account.") 
            
        if command == CLI["Check Balance"]:
            account = input("Enter your account name : ")
            bankAcccount = bank.find_Account(account) 
            print(f"\n Account Info -> {bankAcccount.name} : {bankAcccount.get_balance()}\n" )
            writeLog(f"Account Info of {bankAcccount.name} was showned") 


        if command == CLI["Transfert"]:
            account1 = input("Enter your account name : ")
            account2 = input("Enter the receiver account name : ")
            amount = input("Enter the amount : ")
            amount = int(amount)
            bankAcccount = bank.find_Account(account1) 
            bankAcccount2 = bank.find_Account(account2) 
            bankAcccount.tranfer(bankAcccount2, amount)
            writeLog(f"{bankAcccount.name} do a tranfert ({amount}) at {bankAcccount2.name}") 
            
        if command == CLI["List Accounts"]:
            bank.list_Account()
    except Exception as e:
        print(bcolors.FAIL,"Oups problems, try later \n")
        print(bcolors.ENDC)
        writeLog(f" \"{e}\" run into a problem")

bank.save_to_file()
writeLog(f"Exe quit, infos saved.")     