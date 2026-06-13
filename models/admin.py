from models.student import Student

class Admin(Student):

    def __init__(self, username):
        super().__init__(username)

    def get_role(self):
        return "Admin"
    