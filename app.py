from banking_pkg import account


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")


print("          === Automated Teller Machine ===          ")
balance = 0
while True:
    name = input('Enter name to register: ')
    if len(name) > 10:
        print("Please keep name within 10 characters")
    elif len(name) == 0:
        print("Please enter a valid name!")
    elif len(name) <= 10:
        break

while True:
    pin = input("Enter Pin: ")
    if len(pin) > 4:
        print("Pin may only contain 4 charactes")
    elif len(pin) < 4:
        print("Pin must be at least 4 characters long")
    elif len(pin) == 4:
        break

print(f"{name}, has been registered with a starting balance of {balance}")


while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")

    if name_to_validate == name and pin_to_validate == pin:
        print("Login Succesful")
        break
    print("Invalid Credentials")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
        balance = account.deposit
    elif option == "2":
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == "4":
        account.logout(name)
        break
