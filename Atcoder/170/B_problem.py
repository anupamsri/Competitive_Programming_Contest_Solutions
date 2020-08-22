N, M = map(int,input().split())
for i in range(0, N+1):
    # 足の数
    f = 2 * i + 4 * (N - i)
    if f == M:
        print('Yes')
        break
else:
    print('No')