n, a, b = map(int, input().split())
mod = 10 ** 9 + 7
s = pow(2, n, mod) - 1


def comb(n, r):
    p, q = 1, 1
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * pow(q, mod - 2, mod) % mod


print((s - comb(n, a) - comb(n, b))%mod)
