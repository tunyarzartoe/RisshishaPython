# 入力を受け取る
n = int(input())
a = [int(x) for x in input().split()]

# 答えを保存する変数を用意して適切な初期値で初期化
maximum = -1000000000
minimum = 1000000000

# 配列(リスト)の全要素をチェックするループを書いて
for value in a:
    # 暫定maxを更新
    if value > maximum:
        maximum = value

    # 暫定minを更新
    if value < minimum:
        minimum = value

# 答えを出力する
print(maximum, minimum)

# 入力値
# 5
# 1 2 3 4 5