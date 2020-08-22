x, k,d = map(int, input().split())
x = abs(x)
ans = 0
if x//d>k:
    ans = abs(x-d*k)
else:
    tmp = x//d
    k -= tmp
    x -= tmp*d
    if k%2 == 1:
        ans = abs(x-d)
    else:
        ans = abs(x)
print(ans)