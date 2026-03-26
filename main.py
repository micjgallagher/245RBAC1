import typing
from getpass import getpass
class User:
    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.admin = admin


def authenticate(users,name, password) -> User | None:
    # returns a user object if authentication succeeds and None if it fails
    for account in users:
        if account.username == name and account.password == password: #In a normally app we could not do this
            return account
    return None

def list_users(account, accounts):
    if not account.admin: #This ensures confidentialiaty
        print("Users do not hafe access to user list")
        print("Please log in as an admin")
        return
    for x in accounts:
        print(x.username)

def change_password(account, users):
    password = getpass("Enter your current password")
    if authenticate(users, account.username, password) == None:
        password("Invalid password")
        return #This also supports confidentially
    newpass1 = getpass("Please enter your new password")
    newpass2 = getpass("Please confirm your new password")
    if newpass1 != newpass2:
        print("Passwords do not match")
        return
    account.password = newpass1
    print("succees")

def main():
    users = []
    users.append(User("admin", "adminpassword", True))
    users.append(User("user", "userpassword", False))



#sign in 
    name = input("Please enter your username")
    password = getpass("Please enter your password")

    account = authenticate(users, name, password)
    if account == None:
        print("Invalid Credentials")
        return
    print("Welcome", account.username)

    #menu options
    print("1. List Users")
    print("2. Change Password")

    option = input()

    if option == "1":
        list_users(account, users)
    elif option =="2":
        change_password(account, users)
    else:
        print("invalid option")



main()
