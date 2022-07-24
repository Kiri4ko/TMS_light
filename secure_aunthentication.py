# frontend --------------------------
info = """
USER:\t\t{} 
LAST CMD:\t{}
LIST CMD:\t{}
"""

# database --------------------------
database = {
    "Login": "", "Password_1": "", "Password_2": "",
    "Login_Check": "", "Check_Password": "",
    "User_name": "",
            }

# session ---------------------------
current_user = 'anonimus'

# backend ---------------------------
working = True
cmd = "null"
list_cmd = "singin - New account." \
           "\n\t\tlogin - Sign in account." \
           "\n\t\tlog out - Sign out of the account."

while working:
    print(info.format(current_user, cmd, list_cmd))
    cmd = input("Enter command >> ")
    if cmd == "singin":
        database["User_name"] = input("Enter your user name: ")
        database["Login"] = hash(input("login: "))
        database["Password_1"] = hash(input("password: "))
        database["Password_2"] = hash(input("repeat password: "))
        if database["Password_1"] != database["Password_2"]:
            print("Passwords do not match!\n")
            working = False
    elif cmd == "login":
        database["Login_Check"] = hash(input("login: "))
        database["Check_Password"] = hash(input("password: "))
        current_user = database["User_name"]
        if database["Login"] != database["Login_Check"] \
                or database["Password_2"] != database["Check_Password"]:
            print("No user found!\n")
            working = False
    elif cmd == "log out":
        current_user = 'anonimus'
        working = False
    else:
        working = False
else:
    print(
        "WORK COMPLETED!\nEnter the commands:"
        "\nsingin - New account."
        "\nlogin - Sign in account."
        "\nlog out - Sign out of the account."
    )
