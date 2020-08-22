N = int(input())
A = list(map(int, input().split()))
ANS = [0]*N
for i in A:
    ANS[i-1]+=1
for i in ANS:
    print(i)
