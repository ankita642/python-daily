while True:
    password = input("Enter the secret password: ")
    if password == "python123":
        print("Access Granted!")
        break  # Exits the loop instantly
    print("Wrong password. Try again.\n")
