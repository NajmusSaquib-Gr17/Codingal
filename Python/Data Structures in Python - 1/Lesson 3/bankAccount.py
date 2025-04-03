import random

class BankAccount:
    interest_rate = 0.05
    used_account_numbers = set()

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.account_number = self.generate_account_number()

    def generate_account_number(self):
        while True:
            number = random.randint(10000, 99999)

            if number not in BankAccount.used_account_numbers:
                BankAccount.used_account_numbers.add(number)
                return number
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f'Deposited {amount}. Current balance: ${self.balance}'
        else:
            return 'Deposite amount must be greater than zero'
        
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f'Withdraw ${amount}. Current Balance: ${self.balance}'
            elif self.balance < amount:
                return f'Insufficient Balance'
        else:
            return 'Withdraw amount must be greater than zero'
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f'Interest added: ${interest}. Current Balance: ${self.balance}'
    def account_info(self):
        return (
            f'\n/----------------------------------------------/\n'
            f'Account Number: {self.account_number}\n'
                f'Account Holder name: {self.name}\n'f'Account Balance: {self.balance}\n')
    
acc1 = BankAccount('John Doe', 500)

print(acc1.deposit(1000))
print(acc1.withdraw(450))
print(acc1.apply_interest())
print(acc1.account_info())