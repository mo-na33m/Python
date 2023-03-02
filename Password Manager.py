mp = input("What is your master password? ")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            print(line.rstrip())


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + password + "\n")


while True:
    mode = input("""Would you like to add a new password or view current passwords?
Please type either 'add' 'view' or Q to quit. """).lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode.")
        continue
