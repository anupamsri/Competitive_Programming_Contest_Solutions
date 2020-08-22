S = str(input())
child_num = [1]*len(S)
for i in range(len(S)- 2):
    if S[i] == 'R':
        if S[i + 1] == 'R':
            child_num[i + 2] += child_num[i]
            child_num[i] = 0
for i in range(len(S) - 2):
    if S[len(S) - i -1] == 'L':
        if S[len(S) - i - 2] == 'L':
            child_num[len(S) - i - 3] += child_num[len(S) - i -1]
            child_num[len(S) - i - 1] = 0
print(*child_num)