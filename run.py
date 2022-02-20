import string
import random
from credential import Credential
from user import User


def random_password_generator():
    length = int(input("Enter the length of the password: "))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbol = string.punctuation

    all_above = lower + upper + num + symbol
    temp = random.sample(all_above, length)
    rand_password = ''.join(temp)
    return rand_password


def main():
    print('''
                            ***********************
                            *** Password Locker ***
                            ***********************
    ''')
    print("Welcome to password locker")
    print("Create an account first")
    username_account = input("Username: ")
    password_account = input("Password: ")
    new_user = User(username_account, password_account)
    print("Account created")
    print("")
    print("Read the instruction below to get a better understanding of how the app works")
    print("Use this short codes:")


    while True:
        print("")
        print("cs - to create a new account")
        print("ds - to display your accounts")
        print("fd - to find an account")
        print("del - to delete an account")
        print("ext - to exit the app")
        print("")
        short_code = input("> ").lower().strip()
        if short_code == 'cs':
            print('''
                            *******************
                            *** New Account ***
                            *******************
            ''')
            account_name = input("Account Name: ")
            username = input("Username: ")
            print("-" * 8)
            print("Password")
            print("-"*8)
            print("1:Create my own password")
            print("2:Generate a random password")
            print("")
            password_option = input('Enter option: ')
            if password_option == "1":
                password = input("Password:> ")
            elif password_option == '2':
                password = random_password_generator()
            else:
                print("Please choose an option")

            account_key = int(input("Account Key/Number: "))
            new = Credential(username, password, account_name, account_key)
            new.save_account()

        elif short_code == 'ds':
            accounts = Credential.display_account()
            for account in accounts:
                print("")
                print(f"Account Name: {account.account_name}")
                print(f"Username: {account.username}")
                print(f"Password: {account.password}")
                print(f"Account Key: {account.account_key}")
                print("")
                print("")
            if len(accounts) == 1:
                print(f"You have {len(accounts)} account")
            elif len(accounts) > 1:
                print(f"You have {len(accounts)} accounts")
            print("")

        elif short_code == 'ext':
            ask_ext = input("Are your sure you want to ext?[y/n] ").lower()
            if ask_ext == 'y' or ask_ext == 'yes':

                print("Thank you for your support. Have a great day.")
                print('''
                                ****************
                                *** BYEEEEEE ***
                                ****************
                ''')
                break
            elif ask_ext == 'no' or ask_ext == 'n':
                print("Yes lets go back")
            else:
                print('Enter the given options')
        elif short_code == 'fd':
            print('''
                             ********************
                             *** Find Account ***
                             ********************
             ''')
            ask_key = int(input("Enter the account key of the account you want to search: "))
            account = Credential.find_account(ask_key)
            print("")
            print(f"Account Name: {account.account_name}")
            print(f"Username: {account.username}")
            print(f"Password: {account.password}")
            print("")
        elif short_code == 'del':
            ask_key_del = int(input("Enter the account key of the account you want to delete: "))
            Credential.delete_account(ask_key_del)




if __name__ == "__main__":
    main()