from user import User
print("Welcome to password locker.")
print("Create an account first")
while True:
    username = input("Username: ")
    password = input("Password: ")
    new = User(username, password)
    new.save_account()
    print(User.users[0].password)
    User.display_account()