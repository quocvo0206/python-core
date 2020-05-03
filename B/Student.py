class Student:
    def __init__(self, name, birthday, education, homeTown):
        self._name = name
        self._birthday = birthday
        self._education = education
        self._homeTown = homeTown

    def __init__(self):
        pass

    # getter method
    def get_name(self):
        return self._name

    def get_birthday(self):
        return self._birthday

    def get_education(self):
        return self._education

    def get_homeTown(self):
        return self._homeTown

    # setter method
    def set_name(self, name):
        self._name = name

    def set_birthday(self, birthday):
        self._birthday = birthday

    def set_education(self, education):
        self._education = education

    def set_homeTown(self, homeTown):
        self._homeTown = homeTown

