A,B = map(int, input().split())
for i in range(1009):
    if int(i *0.08) == A and int(i*0.1) == B:
        print(i)
        exit(0)
else:
    print(-1)