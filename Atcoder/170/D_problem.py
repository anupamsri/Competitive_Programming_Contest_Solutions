N=int(input())
A=list(map(int,input().split()))

LIST=[0]*(10**6+1)

for a in A:
    LIST[a]+=1
ANS=0
for i in range(10**6+1):
    if LIST[i]==1:
        ANS+=1
    if LIST[i]!=0:
        for j in range(2*i,10**6+1,i):
            if LIST[j]!=0:
                LIST[j]+=1
print(ANS)
