class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year


class Programmer(Person):
    def __init__(self, name, age, language):
        # self.name = name
        # self.age = age
        super().__init__(name,age)
        self.language = language
        self.languages = {language}
        
kirishima = Programmer("Kirishima", 15, "Ruby")
print(kirishima.name)
print(kirishima.language)        