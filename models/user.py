class User:
    def __init__(self, username):
        self.__username = username

    def get_username(self):
        return self.__username