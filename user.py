class User:
    """
    This is where the user credentials get added
    """
    users = []
    """
    This intialize new user account
    """
    def __init__(self,username, password):
        self.username = username
        self.password = password

        """
        This added the created user to the users list
        """
    def save_account(self):
        User.users.append(self)
