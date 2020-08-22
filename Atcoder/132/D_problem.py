from math import factorial


def combination(n, r):
    if n < r:
        return 0
    else:
        return factorial(n) // (factorial(r) * factorial(n - r))


N, K = map(int, input().split())
MOD = 10 ** 9 + 7
for i in range(1, K + 1):
    ans = combination(N-K+1, i)*combination(K-1,i-1)
    print(ans % MOD)
