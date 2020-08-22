import itertools
N = int(input())
L = list(map(int, input().split()))
L_c = sorted(list(L))
cnt = 0
for i in range(len(L)):
    for j in range(i+1,len(L_c)):
        for l in range(j+1,len(L_c)):
            if L_c[i]!=L_c[j] and L_c[j] !=L_c[l] and L_c[l]<L_c[i] +L_c[j]:
                cnt+=1

print(cnt)