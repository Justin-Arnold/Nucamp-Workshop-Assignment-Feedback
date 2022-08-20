def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f'\nWelcome back {username.title()}!')
            return username.title()  
        print("\nIncorrect password for", username)
        return ""
    print("\nUser not found. Please register.")
    return ""

def register(database, username, password):
    if len(username) > 10:
        print("Username cannot exceed 10 characters")
        return ""
    if len(password) < 5:
        print("Password must be at least 5 characters.")
        return ""

    if username in database:
        print('\nUsername already registered.')
        return ""
    else:
        print(f'\nUsername {username.title()} registered!')
        return username.title()