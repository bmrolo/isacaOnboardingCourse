while True:
    password = input("Enter Password: ")
    length = len(password)

    if length > 8:
        print("Your password meets the requirements")
        break  # exit the loop if a valid password is entered
    else:
        print("Please try again. Password must be at least 8 characters.")
