N,M,X = map(int, input().split())
C = []
A = []
for _ in range(N):
    Cs,*As = map(int,input().split())
    C.append(Cs)
    A.append(As)
INF = float('inf')
ans = INF
for S in range(1<<N):
    B = [0]*M
    cst = 0
    for i in range(N):
        if (S>>i)&1:
            cst+= C[i]
            for j in range(M):
                B[j] += A[i][j]
        if min(B)>=X:
            ans = min(ans,cst)
if ans == INF:
    print(-1)
else:
    print(ans)