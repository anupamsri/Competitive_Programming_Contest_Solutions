from collections import deque

N, M, K = map(int, input().split())
G = [[] for i in range(N)]
NG = [set() for i in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)
    NG[A - 1].add(B - 1)
    NG[B - 1].add(A - 1)

for _ in range(K):
    A, B = map(int, input().split())
    NG[A - 1].add(B - 1)
    NG[B - 1].add(A - 1)
C = [-1] * N
CNT = [0] * N
c = 0
for i in range(N):
    if C[i] >= 0: continue
    Q = [i]
    C[i] = c
    CNT[c] += 1
    while Q:
        x = Q.pop()
        for y in G[x]:
            if C[y] == -1:
                C[y] = C[x]
                CNT[C[y]] += 1
                Q.append(y)
    c +=1
Y = [0] * N
for i in range(N):
    Y[i] = CNT[C[i]] - 1
for i in range(N):
    for j in NG[i]:
        if C[i] == C[j]:
            Y[i] -= 1
print(*Y)
