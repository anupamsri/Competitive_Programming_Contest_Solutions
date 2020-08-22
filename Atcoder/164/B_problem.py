a,b,c,d = map(int, input().split())

while True:
    c = c-b
    if c<=0:
        print('Yes')
        exit()
    a = a-d
    if a<=0:
        print('No')
        exit()