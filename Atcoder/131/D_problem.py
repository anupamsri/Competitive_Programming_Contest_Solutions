N = int(input())
x = [list(map(int, input().split())) for i in range(N)]  # x11 x12
x.sort(key=lambda x: x[1])
limit = 0
for i in range(N):
    limit += x[i][0]
    if limit > x[i][1]:
        print('No')
        exit()
    else:
        pass
else:
    print('Yes')