N = int(input())
A = list(map(int, input().split()))

x = [sum(A) - 2*sum(A[1::2])]
for i in range(1, N):
    x.append(2 * A[i - 1] - x[i - 1])
print(*x)
