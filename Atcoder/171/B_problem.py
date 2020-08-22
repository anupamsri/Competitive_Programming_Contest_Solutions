N, K = map(int,input().split())
p =list(map(int, input().split()))
p = sorted(p)
ans = 0
for i in range(K):
    ans += p[i]
print(ans)