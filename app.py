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
while True:
    name = input("Enter name to register: ")
    if len(name) > 10:
        print("The maximum name length is 10 characters.")
    elif len(name) == 0:
        print("You must enter a name.")
    else:
        break

while True:
    pin = input("Enter PIN: ")
    try:
        pin = str(int(pin))
    except:
        print("Please choose a numeric pin (no letters or symbols).")
        continue
    if len(pin) != 4:
        print("PIN must contain 4 numbers")
    else:
        break

balance = float(0)

print(f'{name} has been registered with a starting balance of ${str(balance)}')

while True:
    name_to_validate = input("Enter name: ")
    pin_to_validate = input("Enter PIN: ")
    if name == name_to_validate and pin == pin_to_validate:
        print("Login successful!")
        break
    else:
        print("Invalid credentials!")

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":
        account.show_balance(balance)
    elif option == "2":
        balance = account.deposit(balance)
        print(f'Your new balance is ${str(balance)}')
    elif option == "3":
        balance = account.withdraw(balance)
        print(f'Your new balance is ${str(balance)}')
    else:
        account.logout(name)
        break
