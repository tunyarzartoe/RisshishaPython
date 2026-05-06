# n = int(input())
# a = [int(x) for x in input().split()]
# k = int(input())

# num_of_k = 0
# for value in a:
#     if value == k:
#         # 答えをインクリメントする
#         value += 1
#         pass
#         num_of_k += 1

# print(num_of_k)

n = int(input())
a = list(map(int, input().split()))
k = int(input())

count = a.count(k)
print(count)

# 入力値
# 5
# 1 2 3 4 5
# 3