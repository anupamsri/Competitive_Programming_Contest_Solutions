import math
A,B,H,M = map(int, input().split())
tmp = (5.5 *(H*60 +M))//360
t = 5.5 *(H*60 +M)-360*tmp
ans = math.sqrt(B**2 + A**2 -math.cos(math.radians(t))*2*A*B)
print(ans)