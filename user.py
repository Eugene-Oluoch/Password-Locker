class User:
    users = []
    def __init__(self,username, password):
        self.username = username
        self.password = password


    def save_account(self):
        User.users.append(self)
