from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123"}
donations = []
authorized_user = ""
total_donations = 0.0

while True:
    show_homepage()

    if authorized_user == "":
        print("You must be logged in to donate")
    else:
        print(f'Logged in as: {authorized_user}')

    option = input("Choose an option: ")

    if option == "1":
        username = input("\nEnter username: ").casefold()
        password = input("Enter password: ")
        authorized_user = login(database, username, password)

    elif option == "2":
        username = input("\nEnter username: ").casefold()
        password = input("Enter password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password

    elif option == "3":
        if authorized_user == "":
            print("\nYou are not logged in")
        else:
            donation_amt = input("\nEnter amount to donate: ")
            if donation_amt.isdigit() and float(donation_amt) > 0:
                total_donations += float(donation_amt)
                donation_string = donate(authorized_user, donation_amt)
                donations.append(donation_string)
            else:
                print("Please enter a valid amount.")

    elif option == "4":
        show_donations(donations)
        print(f'Total = ${str(total_donations)}')

    elif option == "5":
        print("Good bye!")
        break
