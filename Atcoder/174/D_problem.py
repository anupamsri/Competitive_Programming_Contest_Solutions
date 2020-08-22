N = int(input())
S = str(input())
w = S.count('W')
r = S.count('R')
A = 'R'*r+'W'*w
count = 0
for i in range(len(S)):
    if S[i]!=A[i]:
        count += 1

if count%2 ==0:
    print(count//2)
else:
    print(count//2 + 1)