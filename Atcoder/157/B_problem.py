A = [list(map(int, input().split())) for i in range(3)]
N =int(input())
b = [int(input()) for i in range(N)]
for i in b:
    for j in range(3):
        for k in range(3):
            if A[j][k]==i:
                A[j][k]='T'
if A[0][0]=='T' and A[1][0]=='T'and A[2][0]=='T':
    print('Yes')
    exit()
elif A[0][1]=='T' and A[1][1]=='T'and A[2][1]=='T':
    print('Yes')
    exit()
elif A[0][2] == 'T' and A[1][2] == 'T' and A[2][2] == 'T':
    print('Yes')
    exit()
elif A[0][0] == 'T' and A[0][1] == 'T' and A[0][2] == 'T':
    print('Yes')
    exit()
elif A[1][0]=='T' and A[1][1]=='T'and A[1][2]=='T':
    print('Yes')
    exit()
elif A[2][0] == 'T' and A[2][1] == 'T' and A[2][2] == 'T':
    print('Yes')
    exit()
elif A[0][0]=='T' and A[1][1]=='T'and A[2][2]=='T':
    print('Yes')
    exit()
elif A[0][2] == 'T' and A[1][1] == 'T' and A[2][0] == 'T':
    print('Yes')
    exit()
else:
    print('No')