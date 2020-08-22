import math
N, D = map(int, input().split())
x = [list(map(int,input().split())) for i in range(N)]
tmp = 0
ans = 0
for i in range(N):
    for j in range(i + 1,N):
        for d in range(D):
            tmp += (x[i][d] - x[j][d])**2
        tmp = math.sqrt(tmp)
        if tmp.is_integer():
            ans += 1
        tmp = 0
print(ans)