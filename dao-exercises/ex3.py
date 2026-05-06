# 入力を受け取る
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

# 答えを保存する変数を用意して0で初期化
index_of_k = 0

# 配列(リスト)の全要素をインデックス付きでiterateするループを書いて
for i in range(n):
    # 要素がkと一致しているか判定して
    if a[i] == k:
        # 一致していたらインデックスを保存してループを抜ける
        index_of_k = i + 1
        break

# 答えを出力する
print(index_of_k)

# 入力値
# 5
# 1 2 3 4 5
# 3