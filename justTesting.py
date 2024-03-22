class Bank:
    def __init__(self):
        self.accounts = {}

    def modify_account(self, account_number, action, account_details=None):
        if action == 'add' and account_number not in self.accounts:
            self.accounts[account_number] = account_details
        elif action == 'remove' and account_number in self.accounts:
            del self.accounts[account_number]
        elif action == 'change' and account_number in self.accounts:
            self.accounts[account_number] = account_details
        else:
            print("Invalid action or account number")

# Usage
bank = Bank()
bank.modify_account('12345', 'add', {'balance': 1000, 'owner': 'John Doe'})
print(bank.accounts)
bank.modify_account('12345', 'change', {'balance': 500, 'owner': 'Jane Doe'})
print(bank.accounts)
bank.modify_account('12345', 'remove')
print(bank.accounts)
