class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def ram_expansion(self, amount):
        self.ram += amount

pc = PersonalComputer(8, 128)
pc.ram_expansion(8)
print(pc.ram)