N, M = map(int, input().split())
S = []
C = []
for i in range(M):
    s, c = map(int, input().split())
    S.append(s)
    C.append(c)

for i in range(10000):
    tmp = str(i)
    if len(tmp)!=N:
        continue
    flag = True
    for j in range(M):
        if int(tmp[S[j] - 1]) != C[j]:
            flag = False
    if flag == True:
        print(tmp)
        exit()
else:
    print(-1)
