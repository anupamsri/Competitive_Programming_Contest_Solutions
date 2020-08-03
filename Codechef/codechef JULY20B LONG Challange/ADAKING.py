import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

t=int(input())
for i in range(t):
    a=int(input())
    print('O', end='')
    a=a-1
    for k in range(1,9):
        for l in range(1,9):
            if(k==1) and l==1:
                continue
            elif(a):
                a=a-1
                print('.',end='')
            else:
                print('X',end='')
        print()