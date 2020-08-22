N, L = map(int, input().split())
S = []
for i in range(N):
    S.append(L+i)
if 0 in S:
    print(sum(S))
else:
    if S[0]>0:
        print(sum(S)-S[0])
    else:
        print(sum(S)-S[-1])