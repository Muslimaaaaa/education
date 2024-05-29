
import classes
import user_profile
def landing_page(username, password):
    """
    bu funksiya oddiy foydalanuvchining imkoniyatlarini ko'rsatadi

    """
    print("Welcome User page")
    services = input(f"""
        1. Courses
        2. Profile
                >>> """)

    if services == "1":
        classes.Course.get_all_courses()
        back = input("0. Back\n\t>>> ")
        if back == "0":
            return landing_page(username, password)

    elif services == "2":
        return user_profile.profile(username, password)
