n, k = map(int, input().split())
mod = 10 ** 9 + 7
ans = 0
l = [0] * (k + 1)

for i in range(k, 0, -1):
    l[i] = pow(k // i, n, mod)
    print(l)
    for j in range(2 * i, k + 1, i):
        l[i] -= l[j]
        l[i] %= mod
    ans += l[i] * i
    ans %= mod

print(ans)
