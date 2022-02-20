class Credential:
    accounts = []
    def __init__(self, username, password, account_name, account_key):
        self.username = username
        self.password = password
        self.account_name = account_name
        self.account_key = account_key

    def save_account(self):
        Credential.accounts.append(self)

    @classmethod
    def find_account(cls, account_key):
        for account in cls.accounts:
            if account.account_key == account_key:
                return account

    @classmethod
    def display_account(cls):
        return cls.accounts

    @classmethod
    def delete_account(cls, account_key):
        for account in cls.accounts:
            if account.account_key == account_key:
                print(f"Deleted {account.account_name} account with the username {account.username}")
                cls.accounts.remove(account)
