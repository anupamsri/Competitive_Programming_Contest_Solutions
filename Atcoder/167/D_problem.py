N, K = map(int, input().split())
As = list(map(int, input().split()))

Visit = [None] * N
now = 0
n = 0
while Visit[now] is None:
    Visit[now] = n
    now = As[now]-1
    n += 1
    if n == K:
        print(now+1)
        exit()

for _ in range((K-Visit[now]) % (n-Visit[now])):
    now = As[now]-1
print(now+1)
