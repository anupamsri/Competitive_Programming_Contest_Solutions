n = int(input())
A = [int(input()) for i in range(n)]
tmp = sorted(A,reverse=True)
Max = tmp[0]
Second = tmp[1]
for i in range(n):
    if A[i] != Max:
        print(Max)
    else:
        print(Second)
