def show_id(name, value):
    print(f"{name}: {id(value)}")


def increment(x):
    x += 1
    print(x)


n = 813
increment(n)
print(n)