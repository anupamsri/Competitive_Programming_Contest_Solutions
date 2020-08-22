N, X, Y = map(int, input().split())

ans = [0] * N
for i in range(1, N+1):
    for j in range(i+1, N+1):
        d1 = j-i
        d2 = abs(X-i) + 1 + abs(Y-j)
        d = d1 if d1 <= d2 else d2
        ans[d] += 1

for i in range(1,N):
    print(ans[i])
