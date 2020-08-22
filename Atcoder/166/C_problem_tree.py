N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
AB = sorted(AB)
T = [[] for j in range(N)]
for i in range(M):
    T[AB[i][0]-1].append(AB[i][1])
    T[AB[i][1] - 1].append(AB[i][0])
ans = 0
for i in range(N):
    f =True
    for e in T[i]:
        if H[e-1]>=H[i]:
            f = False
    if f:
        ans+=1
print(ans)
