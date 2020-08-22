S = str(input())
# 余りのリスト
counts = [0] * 2019
n, d = 0, 1

for s in S[::-1]:
    n += int(s) * d
    d *= 10
    n %= 2019
    #2019より大きいモノをかけない
    d %= 2019
    counts[n] += 1
ans = counts[0]
for count in counts:
    ans += count * (count - 1) // 2
print(ans)
