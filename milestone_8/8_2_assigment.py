# -*- coding: utf-8 -*-
"""8_2_assigment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14i8prR2HfX0Q6ZtVHQO8LS6wLFQaKwHS

# Assignment 8.2

> Replace all TODOs with your code.
>
> Do not change any other code and do not add/remove cells!

## Inheritance

### Task 1

Define a base class named `Account` to a general bank account.

The class should include an initialization method (`__init__`), taking into account the number and holder name and methods for depositing money to the account and withdrawing from it. Do not forget to ensure that the account never has a negative balance.

String representation (`__str__`) should be an abstract method (throw a corresponding error if it is called on the base `Account` class
"""

class Account:
    def __init__(self, number, holder_name):
        self.number = number
        self.holder_name = holder_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance or invalid withdrawal amount")

    def __str__(self):
        raise NotImplementedError("This method should be implemented by subclasses")

"""### Task 2

Derive a `CurrentAccount` subclass from the `Account` base class and provide its own implementation for the `__str__` method. The text representation should mention the type of account, account number, and remaining balance.
"""

class CurrentAccount(Account):
    def __str__(self):
        return f"Current Account - Account Number: {self.number}, Holder: {self.holder_name}, Balance: {self.balance}"

"""### Task 3

Derive a `SavingsAccount` subclass from the `Account` base class and provide its implementation for the `__str__` method. When initializing objects of this class, the caller must provide the `interest_rate` parameter.

 The text representation should mention the type of account, interest rate, account number, and remaining balance.

Provide additional method `add_interest` that adds interest based on `interest_rate`:
$$new\_balance = old\_balance + old\_balance * interest\_rate$$
"""

class SavingsAccount(Account):
    def __init__(self, number, holder_name, interest_rate):
        super().__init__(number, holder_name)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Savings Account - Interest Rate: {self.interest_rate*100}%, Account Number: {self.number}, Holder: {self.holder_name}, Balance: {self.balance}"

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

"""### Task 4

Create an array with different accounts, add/withdraw money from some of them, iterate over the array, and print the text representation of each.
"""

accounts = [
    CurrentAccount(1001, "User 1"),
    SavingsAccount(1002, "User 2", 0.03),
    CurrentAccount(1003, "User 3"),
    SavingsAccount(1004, "User 4", 0.05)
]

accounts[0].deposit(500)
accounts[1].deposit(1000)
accounts[2].deposit(200)
accounts[3].deposit(1500)

accounts[0].withdraw(100)
accounts[1].add_interest()

for account in accounts:
    print(account)