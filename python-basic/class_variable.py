class Person:
    binomen = "homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year

    def add_and_print_age(self, year):
        self.add_age(year)
        print(self.age)

print(Person.binomen)   

kirishima = Person("Kirishima",15)
print(kirishima.binomen)