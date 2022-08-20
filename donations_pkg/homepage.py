def show_homepage():
    print("          === DonateMe Homepage ===       ")
    print("------------------------------------------")
    print("| 1.    Login     | 2.    Register       |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.    Show Donations |")
    print("------------------------------------------")
    print("|                5.  Exit                |")
    print("------------------------------------------")

def donate(username):
    donation_amt = input("\nEnter amount to donate: ")
    print(f'{username} donated ${donation_amt}')
    print("Thank you for your donation!")
    donation_string = username + " donated $" + donation_amt
    return donation_string

def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently there are no donations.")
    else:
        for x in donations:
            print(x)
