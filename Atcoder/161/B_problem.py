N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
ans = sum(x >= (sum(A) / (4 * M)) for x in A)
print('No' if ans < M else 'Yes')

