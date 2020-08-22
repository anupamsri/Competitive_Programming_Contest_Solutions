N,A,B = map(int, input().split())
Count = N//(A+B)
if N-(A+B)*Count >= A:
    print(A*Count+A)
else:
    print(A*Count+(N-(A+B)*Count))