class PersonalComputer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage


class Laptop(PersonalComputer):
    def __init__(self, ram, storage, key_layout, battery=50):
        super().__init__(ram, storage)
        self.key_layout = key_layout
        self.battery = battery
        self.batteries = {battery}

    # 以下にコードを記述
    def charge(self, battery):
        self.battery += battery
        self.batteries.add(self.battery)

laptop_pc = Laptop(8, 128, "jis")
laptop_pc.charge(50)
print(laptop_pc.battery)
print(laptop_pc.batteries)
