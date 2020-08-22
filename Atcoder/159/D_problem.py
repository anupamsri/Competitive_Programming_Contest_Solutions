import collections

n = int(input())
a = list(map(int, input().split()))

C = collections.Counter(a)
total = 0
for i in C.keys():
    total += C[i] * (C[i] - 1) // 2
for i in range(n):
    A = a[i]
    print(total - C[A] + 1)
