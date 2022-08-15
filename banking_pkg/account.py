
def show_balance(balance):
    print(balance)


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return balance + float(amount)


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    amount = float(amount)
    if amount > balance:
        print(f'The amount you wish to withdraw exceeds your current balance.')
        return balance
    else:
        return balance - amount


def logout(name):
    print("Goodbye", name)
