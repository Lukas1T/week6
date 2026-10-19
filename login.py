password = "python123"
logged_in = False

while logged_in == False:
    user_input = input("Enter the password: ")

    if user_input == password:
        print("Öoggin successful.")
        logged_in = True
    else: 
        print("Login failed.Try again.")


