def saveUserToFile(email,password):
    LogMessage = str(email) + ':' + str(password)
    print("Account created: "+ LogMessage)
    with open('Accounts/Accounts.txt','a') as file:
        file.write("Account created: " + LogMessage + "\n")


