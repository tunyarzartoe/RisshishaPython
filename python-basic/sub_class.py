class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year
class Programmer(Person):
    def __init__(self, name, age, programming_language):
        super().__init__(name, age)
        self.programming_language = programming_language

kirishima = Programmer("Kirishima",15,"Python")
print(f"{kirishima.name},{kirishima.age},{kirishima.programming_language}")