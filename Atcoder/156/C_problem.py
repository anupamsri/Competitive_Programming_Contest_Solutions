import math
N = int(input())
X = list(map(int, input().split()))
X = sorted(X)
ans = 10**9+7
for i in range(1,100):
    tmp = 0
    for j in X:
        tmp += (j-i)**2
    ans = min(ans,tmp)
print(ans)