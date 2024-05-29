from classes import User
def login():
    """ bu funksiya saytdan login qilish orqali foydalanishga imkon beradi"""
    print("Login Page")
    username = input("Username: ")
    password = input("Password: ")
    if User.check_user(username, password) is False:
        print("kechirasiz bizda bunday foydalanuvchi mavjud emas:")
        return login()


def mainmenu():
    optionone = int(input("Choose 1 to sign in and choose 2 to log in"))
    if optionone == 1:
        register_uz()
    elif optionone == 2:
        login()
    else:
        print("Option is not available")
        mainmenu()

    exit()

def exit():
    answer = str(input("Do you still want to conduct transaction ? yes or no"))
    if answer == "yes":
        login()
    elif answer == "No":
        print("Thank you for using this app")
    else:
        print("Option is not available")
        mainmenu()


mainmenu()]