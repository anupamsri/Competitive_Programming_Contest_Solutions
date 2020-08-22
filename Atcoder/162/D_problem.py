N = int(input())
S = str(input())

ans = S.count('R')*S.count('G')*S.count('B')

for i in range(N):
    for j in range(i+1,N):
        k = 2*j - i
        if k>=N:
            break
        if S[i]!=S[j] and S[i]!=S[k] and S[j]!=S[k]:
            ans -=1

print(ans)