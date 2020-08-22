from collections import deque
S = str(input())
Q = int(input())
Qer = [list(map(str,input().split())) for i in range(Q)]
flag = True
anss = deque(S)
for i in range(Q):
    if Qer[i][0] == "1":
        flag = not flag
    else:
        if flag ==True:
            if Qer[i][1] =="1":
                anss.appendleft(Qer[i][2])
            else:
                anss.append(Qer[i][2])
        else:
            if Qer[i][1] =="2":
                anss.appendleft(Qer[i][2])
            else:
                anss.append(Qer[i][2])
anss=''.join(anss)
if flag == True:
    print(anss)
else:
    anss = anss[::-1]
    print(anss)