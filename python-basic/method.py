class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_age(self, year):
        self.age += year


def add_age(year):
    print("Person クラスの外の関数です。")


kirishima = Person("Kirishima", 15)

kirishima.add_age(3)
print(f"{kirishima.age} 歳")

add_age(10)
print(f"{kirishima.age} 歳")