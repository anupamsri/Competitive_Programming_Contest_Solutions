import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
    
# cook your dish here
def digit(num):
    ans=0
    while num>0:
        ans=ans+(num%10)
        num=num//10
    return ans

t=int(input())
for i in range(t):
    rounds=int(input())
    chefwin, mortywin = 0, 0
    for ii in range(rounds):
        one,two=map(int,input().split())
        # print(one,two)
        chef=digit(one)
        morty=digit(two)
        if chef> morty:
            chefwin += 1
        elif chef < morty:
            mortywin += 1
        else:
            chefwin += 1
            mortywin += 1

    if chefwin > mortywin:
        print(0, chefwin)
    elif chefwin < mortywin:
        print(1, mortywin)
    else:
        print(2, chefwin)
            
            