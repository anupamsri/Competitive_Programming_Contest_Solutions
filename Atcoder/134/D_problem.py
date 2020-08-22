M = int(input())
a = list(map(int, input().split()))

box = [0]*M
for i in range(M)[::-1]:
    s = sum(box[i::i + 1])
    if s % 2 != a[i]:
        box[i] = 1
M = sum(box)
print(M)
if M != 0:
    for i, j in enumerate(box):
        if j == 1:
            print(i + 1)