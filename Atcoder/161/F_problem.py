n = int(input())


def divisor(n):
    fac = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            fac.append(i)
            if i * i != n:
                fac.append(n // i)
    return sorted(fac)


ans = len(divisor(n - 1)) - 1
lst = divisor(n)
for i in lst:
    tmp = n
    if i == 1:
        continue
    while tmp % i == 0:
        tmp //= i
    if tmp % i == 1:
        ans += 1

print(ans)
