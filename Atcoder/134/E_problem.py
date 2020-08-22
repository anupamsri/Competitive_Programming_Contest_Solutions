from bisect import bisect_right
N = int(input())
A = [int(input()) for _ in range(N)]
dp = [10**10] * N
for a in A:
    a = -a
    dp[bisect_right(dp, a)] = a
ans = N - dp.count(10**10)
print(ans)
