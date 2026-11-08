import getpass

u = "gab"
p = "huehue"

isLogin = False

while isLogin == False:

    user = input("Enter you username -->  ")
    pword = getpass.getpass("Enter you password -->  ")

    if user == u and pword == p:
        print("LOGIN SUCCESSFULLY!")

    else:
        print("LOGIN FAILED.")
        isLogin == False
        continue

    print("WELCOME, ", u, "!")
    break        