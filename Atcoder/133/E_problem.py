n, k = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b)
    G[b - 1].append(a)
print(G)
mod = 10 ** 9 + 7
stack = [0]
visited = [True] + [False] * n
ans = k
while stack:
    v = stack.pop()
    c = k - 2 if v != 0 else k - 1
    for i in G[v]:
        if not visited[i]:
            ans = (ans * c) % mod
            c -= 1
            stack.append(i)
            visited[i] = True
print(ans)
