import classes

def settings(username, password):
    services = input("""
        1. First Name
        2. Last Name
        3. Password
        0. Back
        >>> """)

    if services == "1":
        new_first_name = input("Enter new First Name: ")
        print(classes.User.set_first_name(new_first_name, username, password, "first_name"))

    elif services == "2":
        new_last_name = input("Enter new Last Name: ")
        print(classes.User.set_first_name(new_last_name, username, password, "last_name"))

    elif services == "3":
        new_password = input("Enter new password: ")
        print(classes.User.set_first_name(new_password, username, password, "password"))
def profile(username, password):
    menu = input("""
        1. My Courses
        2. Settings
        0. Back
            >>> """)

    if menu == "1":
        for course in classes.User.active_course(username, password):
            print(course)

    elif menu == "2":
        return settings(username, password)

