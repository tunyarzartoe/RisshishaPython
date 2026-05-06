n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

num_of_k = 0
for value in a:
    if value == k:
        num_of_k += 1

print(num_of_k)

# 入力値
# 5
# 1 2 3 4 5
# 3