def rec_product(n):
    if n <= 1:
        return 1
    return n * rec_product(n - 1)

print(rec_product(10))
