print("Authentication vs Authorization Demo")

username = input("Enter username: ")

if username == "vaibhav":
    print("Authentication Successful")

    role = "Employee"

    if role == "Admin":
        print("Authorization: Full Access")
    else:
        print("Authorization: Limited Access")
else:
    print("Authentication Failed")