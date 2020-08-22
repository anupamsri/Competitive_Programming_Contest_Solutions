N = int(input())
A = list(map(int, input().split()))
LIST = [0]*(100001)
Q = int(input())


b =[0]*Q
c =[0]*Q
for i in range(Q):
    b[i], c[i] = map(int, input().split())

for i in A:
    LIST[i]+=1

s = sum(A)

for i in range(Q):
    s += LIST[b[i]]*(c[i]-b[i])
    LIST[c[i]]+=LIST[b[i]]
    LIST[b[i]] = 0
    print(s)
