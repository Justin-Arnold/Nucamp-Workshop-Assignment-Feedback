def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f'\nWelcome back {username.title()}!')
            return username.title()  
        print("\nIncorrect password for", username)
        return ""
    print("\nUser not found. Please register.")
    return ""

def register(database, username):
    if username in database:
        print('\nUsername already registered.')
        return ""
    else:
        print(f'\nUsername {username.title()} registered!')
        return username.title()