print("Login System")

username = input("Enter username: ")
password = int(input("Enter password: "))

if username == "admin":
    if password == 1234:
        print("Login successful")
    else:
        print("Password is wrong")
else:
    print("Username is wrong")