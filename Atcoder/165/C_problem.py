import itertools
N,M,Q = map(int, input().split())
L = [list(map(int, input().split())) for i in range(Q)]
ans = 0
for A in itertools.combinations_with_replacement([i for i in range(1,M+1)],N):
    sorted(A)
    pre_ans = 0
    for i in range(Q):
        a,b,c,d = L[i]
        if A[b-1] - A[a-1] == c:
            pre_ans += d
        ans = max(ans,pre_ans)
print(ans)