X,N= map(int,input().split())
p = list(map(int, input().split()))
p = sorted(p)
ans_tmp = 10**9+7
ans = 0
if N==0:
    print(X)
else:
    if X not in p:
        print(X)
        exit()
    else:
        tmp1,tmp2 = X-1,X+1
        while True:
            if tmp1 not in p:
                print(tmp1)
                exit()
            if tmp2 not in p:
                print(tmp2)
                exit()
            tmp1 -= 1
            tmp2 += 1