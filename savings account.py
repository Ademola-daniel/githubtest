from account import Account


class SavingsAccount(Account):
    def __init__(self, balance=50000):
        super().__init__(balance)
        self.interest_rate = 0.005
        self.withdrawal_limit = 700000

    def deposit(self, amount):
        super().deposit(amount)
        self._balance += amount * self.interest_rate

    def withdraw(self, amount):
        if amount <= self.withdrawal_limit:
            return super().withdraw(amount)
        else:
            print("Withdrawal amount exceeds limit")
            return 0

# Create an instance of a Savings Account
savings_account = SavingsAccount()

# Withdraw 1000 from the savings account
withdraw_amount = 1000
withdrawn_amount = savings_account.withdraw(withdraw_amount)

print("Amount withdrawn from savings account:", withdrawn_amount)
print("Current balance in savings account:", savings_account.get_balance())
