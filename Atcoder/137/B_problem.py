K, X = map(int, input().split())
ans = []
num = X - K
for i in range(K*2-1):
    num += 1
    ans.append(num)
print(*ans)