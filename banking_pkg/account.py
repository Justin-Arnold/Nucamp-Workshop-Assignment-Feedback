def show_balance(balance):
    print(float(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    return(balance + float(amount))


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    if float(amount) > balance:
        print("Insufficient Funds")
        return balance
    else:
        print(balance)
    return(balance - float(amount))


def logout(name):
    print("Goodbye", name, "!")
