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

main()
