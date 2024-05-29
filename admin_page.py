import classes
def landing_page(username, password):
    """
    bu funksiya sayt adminining imkoniyatlarini ko'rsatadi

    """
    print("Welcome Admin page")
    services = input(f"""
        1. Users
        2. Courses
            >>> """)
    if services == "1":
        classes.User.all_users()
        return landing_page(username, password)
    elif services == "2":
        back = input("0. Back\n\t>>> ")
        if back == "0":
            return classes.Course.get_all_courses()