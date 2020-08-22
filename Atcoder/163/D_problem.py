N,K = map(int,input().split())
mod = 10**9 + 7
ans = 0
for i in range(K,N+2):
    M = i*(2*N-i+1)//2
    m = i*(i-1)//2
    ans += (M - m + 1)
print(ans % mod)
