from models.user import User

class Student(User):

    def __init__(self, username):
        super().__init__(username)

    def get_role(self):
        return "Student"