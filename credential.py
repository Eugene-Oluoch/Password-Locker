class Credential:
    """
    This is where the account get stored
    """
    accounts = []
    """
    This where the account gets initialised
    """
    def __init__(self, username, password, account_name, account_key):
        self.username = username
        self.password = password
        self.account_name = account_name
        self.account_key = account_key

    """
    This where the initialised account get appended to the accounts list
    """
    def save_account(self):
        Credential.accounts.append(self)

    """
    This loops through the accounts list and displays the account with the provided account_key
    """
    @classmethod
    def find_account(cls, account_key):
        for account in cls.accounts:
            if account.account_key == account_key:
                return account
    """
    This loops through the accounts list and displays all the accounts available
    """
    @classmethod
    def display_account(cls):
        return cls.accounts
    
    """
    This deletes the account with the provided account_key
    """
    @classmethod
    def delete_account(cls, account_key):
        for account in cls.accounts:
            if account.account_key == account_key:
                print(f"Deleted {account.account_name} account with the username {account.username}")
                cls.accounts.remove(account)
