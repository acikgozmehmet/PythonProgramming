from abc import ABCMeta, abstractmethod
import random 

class Account(metaclass = ABCMeta):

    @abstractmethod    
    def createAccount():
        return 0
    
    @abstractmethod
    def authenticate():
        return 0
    
    @abstractmethod
    def withdraw():
        return 0


    @abstractmethod
    def deposit():
        return 0
    
    @abstractmethod
    def displayBalance():
        return 0
    


class SavingsAccount(Account):
    
    def __init__(self):
        self.savingsAccounts = {}
        
        
    
    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[self.accountNumber][0] == name:
                print("Authentication is successfull")
                self.accountNumber = accountNumber
                return True
            else :
                print("Authentication Failed")
                return False
        else:
                print("Authentication Failed")
                return False
            
                
    
    
    
    def createAccount(self,name, initialDeposit):
        self.accountNumber = random.randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account created. Your account number is ", self.accountNumber)
    

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal succesfull")
            self.displayBalance()
            
        
    
    def deposit(self, depositAmount):
        if depositAmount > 0 :
            self.savingsAccounts[self.accountNumber][1] += depositAmount
            print("deposit successfull")
            self.displayBalance()
        else:
            print("Enter valid amount")


    def displayBalance(self):
        print("Availabel balance", self.savingsAccounts[self.accountNumber][1])
        
    
        
    def chooseSavingAccount(self):
        print("choose savings account")
        name = input("Please enter your name: ")
        accountNumber = int(input("Please enter your account number"))
        authenticationStatus = self.authenticate(name, accountNumber)
        if authenticationStatus:
            self.menuSavingAccount()
        else:
            self.menu()
        

    
    def menu(self):
        while True:
            print("\n1. Create a new savings account")
            print("2. Choose an existing savings account")
            print("3. Exit")
            userchoice = int(input())
            if userchoice is 1:
                name = input("Please enter your name: ")
                deposit = float(input("Please enter your deposit: $"))
                self.createAccount(name, deposit)
            elif userchoice is 2:
                self.chooseSavingAccount()
            elif userchoice is 3:
                quit()
            else:
                print("Select an option")
    
    
    
    def menuSavingAccount(self):
        while True:
            print("\n1. Withdraw ")
            print("2. Deposit")
            print("3. Display balance")
            print("4. Exit")
            userchoice = int(input())
            if userchoice is 1:
                withdrawalAmount = float(input("Enter the amount to withdraw"))
                self.withdraw(withdrawalAmount)
            elif userchoice is 2:
                depositAmount = float(input("Enter the amount to deposit"))
                self.deposit(depositAmount)
            elif userchoice is 3:
                self.displayBalance()
            elif userchoice is 4:
                quit()                
            else:
                print("Select an option")
           
    

        
savingsAccount = SavingsAccount()
savingsAccount.menu()