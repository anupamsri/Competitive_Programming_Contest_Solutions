from collections import deque

N, M = map(int, input().split())
G = [[] for i in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    G[B-1].append(A-1)
#bfsで探索
T = [-1]*N
que = deque()
que.append(0)

while que:
    v = que.popleft()
    for e in G[v]:
        if T[e] == -1:
            T[e] = v+1
            que.append(e)
print("Yes")
print(*T[1:], sep="\n")
