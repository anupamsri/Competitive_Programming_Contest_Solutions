from collections import deque
K = int(input())
q = deque()

mod = 0
for i in range(1,10):
    q.append(i)
for _ in range(K):
    x = q.popleft()
    mod = x % 10
    if mod != 0:
        q.append(x * 10 + mod - 1)
    q.append(x * 10 + mod)
    if mod != 9:
        q.append(x * 10 + mod + 1)
print(x)


