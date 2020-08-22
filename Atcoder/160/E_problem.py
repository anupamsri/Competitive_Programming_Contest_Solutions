X, Y, A, B, C = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
p = sorted(p)[::-1]
q = sorted(q)[::-1]
r = sorted(r)[::-1]
ans = sorted(p[:X] + q[:Y] + r)[::-1]
print(sum(ans[:X + Y]))
