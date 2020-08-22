A,B,C,K = map(int, input().split())
ans = 0
if K - A>=0:
    ans += A
    if K-A-B<=0:
        pass
    else:
        ans -= (K-A-B)
else:
    ans += K
print(ans)