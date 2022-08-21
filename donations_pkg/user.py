def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f'\nWelcome back {username.title()}!')
            return username.title()  
        print("\nIncorrect password for", username)
        return ""
    print("\nUser not found. Please register.")
    return ""

def credential_validation(username, password):
    validation_message = []
    if len(username) > 10:
        validation_message.append("Username cannot exceed 10 characters.")
    if not username.isalnum(): 
        validation_message.append("Username cannot include symbols.")
    if not username[0].isalpha():
        validation_message.append("Username must begin with a letter.")
    if len(password) < 5:
        validation_message.append("Password must be at least 5 characters.")
    for message in validation_message:
        print(message)
    if validation_message == []:
        return True
    else:
        return False



def register(database, username):
    if username in database:
        print('\nUsername already registered.')
        return ""
    else:
        print(f'\nUsername {username.title()} registered!')
        return username.title()