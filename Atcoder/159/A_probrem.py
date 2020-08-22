import math
N, M = map(int, input().split())
if(N>=2):
    n = math.factorial(N) // (math.factorial(N - 2) * math.factorial(2))
else:
    n = 0

if(M>=2):
    m = math.factorial(M) // (math.factorial(M - 2) * math.factorial(2))
else:
    m = 0
print(n+m)
