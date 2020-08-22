S = str(input())
count =0
flag = 1
if S[1]=='R':
    if S[0]=='R'and S[2]=='R':
        count= 3
    elif S[0]=='R'and S[2]=='S':
        count= 2
    elif S[0]=='S'and S[2]=='R':
        count= 2
    elif S[0] == 'S' and S[2] == 'S':
        count = 1
else:
    if S[0]=='R'and S[2]=='R':
        count= 1
    elif S[0]=='S'and S[2]=='R':
        count= 1
    elif S[0]=='R'and S[2]=='S':
        count= 1
    elif S[0] == 'R' and S[2] == 'R':
        count = 1
print(count)