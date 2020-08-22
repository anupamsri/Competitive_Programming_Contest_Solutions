N,K = map(int, input().split())
ans = 0
while True:
    if N ==0:
        break
    N = N//K
    ans += 1
print(ans)