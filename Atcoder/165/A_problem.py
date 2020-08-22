K = int(input())
a, b = map(int, input().split())
for i in range(a,b+1):
    if(i % K)==0:
        print('OK')
        exit()
else:
    print('NG')