class Word:
    def __init__(self, english, turkish):
        self.__english = english
        self.__turkish = turkish

    def get_english(self):
        return self.__english

    def get_turkish(self):
        return self.__turkish