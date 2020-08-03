import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")

t = int(input())
arr = []
for i in range (t):
    n = int(input())
    listis = list(int(num) for num in input().strip().split())
    counting = 0
    j1=1    
    for i in range(len(listis)):
        if j1<len(listis):
            if (listis[i]==listis[j1]):
                k=0
            else:
                k = abs(listis[i]-listis[j1])-1
                i=i+1
                j1=j1+1
                counting=counting+k
    arr.append(counting)
for ll in range (t):
     print("%d"%(arr[ll]))