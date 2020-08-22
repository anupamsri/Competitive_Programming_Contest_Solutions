N, M = map(int, input().split())
H = list(map(int, input().split()))
AB = [list(map(int, input().split())) for _ in range(M)]
T = [0] * N
for i in range(M):
    if H[AB[i][0] - 1] == H[AB[i][1]-1]:
        T[AB[i][0] - 1] = 1
        T[AB[i][1] - 1] = 1
    else:
        if H[AB[i][0] - 1]>H[AB[i][1]-1]:
            T[AB[i][1] - 1] = 1
        else:
            T[AB[i][0] - 1] = 1
print(T.count(0))