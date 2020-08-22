N, K = map(int, input().split())
d = []
A =[0]*N
for i in range(K):
    d=input()
    a = list(map(int, input().split()))
    for i in a:
        A[i-1]+=1
print(A.count(0))
