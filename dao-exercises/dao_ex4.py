# 入力を受け取る
n = int(input())
a = [int(x) for x in input().split()]

# 答えを保存する変数を用意して0で初期化
index_of_even = 0

# 配列(リスト)の全要素をインデックス付きでiterateするループを書いて
for i in range(n):
    # 要素が偶数かどうか判定して
    if a[i] % 2 == 0:
        # 偶数だったらインデックスを保存してループを抜ける
        index_of_even = i + 1
        break

# 答えを出力する
print(index_of_even)

# 入力値
# 5
# 1 2 3 4 5