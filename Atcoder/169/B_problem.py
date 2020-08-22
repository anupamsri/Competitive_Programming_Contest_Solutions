N = int(input())
A = list(map(int, input().split()))
ans = 1
if 0 in A:
    print(0)
    exit()
for i in A:
    ans *=i
    if ans >10**18:
        print(-1)
        exit()
print(ans)