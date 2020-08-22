N, K, C = map(int, input().split())
S = str(input())
A = [0] * K
B = [0] * K
a = 0
b = N - 1
for i in range(K):
    j = K - 1 - i
    while S[a] == 'x':
        a += 1
    while S[b] == 'x':
        b -= 1
    A[i] = a
    a += 1 + C
    B[j] = b
    b -= 1 + C
for i in range(K):
    if A[i] == B[i]:
        print(A[i] + 1)