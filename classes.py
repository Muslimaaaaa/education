import json
from datetime import datetime
import admin_page
import user_page


class User:
    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__password = password
        self.status = "user"
        self.create_date = f"{datetime.now()}"

    @staticmethod
    def all_users():
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)

            for user in data["users"]:
                print(f"""
                           First Name: {user["first_name"]}
                           Last Name: {user["last_name"]}
                       """)

    @property
    def get_password(self):
        return self.__password

    def full_info(self):
        return f"""
            First Name: {self.first_name}
            Last Name: {self.last_name}
            Username: {self.username}
            Password: {self.get_password}
        """

    @staticmethod
    def active_course(username, password):
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    courses = user["courses"]
                    return courses

    def save(self):
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)

        with open("data/users.json", "w") as f:
            new_user = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "username": self.username,
                "password": self.get_password,
                "status": self.status,
                "create_date": self.create_date
            }
            data["users"].append(new_user)
            json.dump(data, f, indent=6)
        print("Register Successfully")

    @staticmethod
    def check_user(username, password):
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            for user in data["users"]:
                if user["username"] == username and user["password"] == password:
                    if user["status"] == "admin":
                        return admin_page.landing_page(username, password)
                    else:
                        return user_page.landing_page(username, password)
            return False

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @staticmethod
    def set_first_name(new_first_name, username, password, atribut):
        with open("data/users.json", encoding="utf-8") as file:
            data = json.load(file)
            users = data["users"]
            for user in users:
                if user["username"] == username and user["password"] == password:
                    check_user = user
                    # print(user)
            users.remove(check_user)
            check_user[atribut] = new_first_name
            users.append(check_user)
            data["users"] = users

        with open("data/users.json", "w") as f:
            json.dump(data, f, indent=6)

        return "Successfully change"


class Course:
    def __init__(self, title: str, description: str, price: float, modules: int, mentor: str):
        self.title = title
        self.description = description
        self.price = price
        self.modules = modules
        self.mentor = mentor
        self.create_date = f"{datetime.now()}"

    @staticmethod
    def get_all_courses():
        with open("data/courses.json", encoding="utf-8") as file:
            data = json.load(file)
            for course in data["courses"]:
                print(f"""
                        Title: {course["title"]}
                        Description: {course["description"]}
                        price: {course["price"]}
                        modules: {course["modules"]}
                        Title: {course["mentor"]}
                    """)


class Person(User):
    def __init__(self, first_name, last_name, username, password, birth_date, phone_number):
        User.__init__(self, first_name, last_name, username, password)
        self.birth_date = birth_date
        self.phone_number = phone_number

    def full_info(self):
        return f"""
                        First Name: {self.first_name}
                        Last Name: {self.last_name}
                        Username: {self.username}
                        Password: {self.get_password}
                        Birth Date: {self.birth_date}
                        Phone Number: {self.phone_number}
                    """
