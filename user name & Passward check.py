# 19. Username and password check
stored_user, stored_pass = "admin", "1234"
user = input("Enter username: ")
password = input("Enter password: ")
if user == stored_user and password == stored_pass:
    print("Login successful")
else:
    print("Login failed")