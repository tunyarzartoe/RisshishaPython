def show_id(name, value):
    print(f"{name}: {id(value)}")

a = [1, 2, 3]
show_id("更新前の a", a)

a += [4, 5, 6]
show_id("更新後の a", a)

b, c = [1, 2, 3], [1, 2, 3]
show_id("リスト 1", b)
show_id("リスト 2", c)