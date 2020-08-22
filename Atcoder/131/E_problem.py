N, K = map(int, input().split())
if (N -1)*(N -2)//2 < K:
    print(-1)
    exit()
else:
    M = (N -1)*(N -2)//2 - K + (N - 1)
    print(M)
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            print(i,j)
            M-=1
            if M ==0:
                exit()
