def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

import math
K = int(input())
ans_list = []
ans = 0
for i in range(1, K + 1):
    for j in range(1,K+1):
        ans_list.append(math.gcd(i,j))
for i in range(1,K+1):
    for j in range(0,len(ans_list)):
        ans += math.gcd(i,ans_list[j])

print(ans)
