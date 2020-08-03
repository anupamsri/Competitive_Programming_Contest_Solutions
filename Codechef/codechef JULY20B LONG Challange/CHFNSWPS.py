import sys
from os import path
if(path.exists('input.txt')):
    sys.stdin = open("input.txt","r")
    sys.stdout = open("output.txt","w")
test = int(input())

for _ in range(test):
    n = int(input())
    array1 = list(map(int, input().split()))
    array2 = list(map(int, input().split()))
    exitingflagis = False
    minimum = 2 << 30
    ele11ments11 = set()
    lengthisA = 0
    lengthisB = 0
    movingtowardsB = []
    movingtowardsA = []
    frequencyis2 = {}
    frequencyis1 = {}
    
    for i in array1:
        if (i in frequencyis1):
            frequencyis1[i] =frequencyis1[i] + 1
        else:
            frequencyis1[i] = 1
            frequencyis2[i] = 0
            ele11ments11.add(i)

    for i in array2:
        if (i in frequencyis2):
            frequencyis2[i] = frequencyis2[i]+1
        else:
            frequencyis2[i] = 1
            if i not in ele11ments11:
                frequencyis1[i] = 0
                ele11ments11.add(i)

    for i in ele11ments11:
        CC1111 = frequencyis1[i]
        CC2222 = frequencyis2[i]
        frequencyis = CC1111 + CC2222
        if((CC1111 + CC2222) != ((frequencyis >> 1) << 1)):
            exitingflagis = True
            break

        if(minimum > i):
            minimum = i

        if(CC1111 < CC2222):
            for j in range((CC2222 - CC1111) >> 1):
                movingtowardsB.append(i)
                lengthisB = lengthisB +1
        elif(CC2222 < CC1111):
            for j in range((CC1111 - CC2222) >> 1):
                movingtowardsA.append(i)
                lengthisA = lengthisA +1

    if(lengthisA != lengthisB):
        exitingflagis = True

    if(exitingflagis):
        print(-1)
        continue

    movingtowardsA.sort()
    movingtowardsB.sort()

    minimum = minimum *2
    lessenessofminimumofA = 0
    lessenessofminimumofB = 0
    
    
    for i in movingtowardsA:
        if i > minimum:
            break
        lessenessofminimumofA = lessenessofminimumofA+1
    greatnesofMinimumofA = lengthisA - lessenessofminimumofA

    for i in movingtowardsB:
        if i > minimum:
            break
        lessenessofminimumofB = lessenessofminimumofB+1
    greatnessofminimumB = lengthisB - lessenessofminimumofB

    paisaisgiven = 0

    if(lessenessofminimumofA <= greatnessofminimumB):
        for i in movingtowardsA[:lessenessofminimumofA]:
            paisaisgiven = paisaisgiven+i
        for i in movingtowardsB[:lessenessofminimumofB]:
            paisaisgiven = paisaisgiven +i
        paisaisgiven += (minimum * (greatnesofMinimumofA - lessenessofminimumofB))

    else:
        for i in movingtowardsA[:(greatnessofminimumB)]:
            paisaisgiven = paisaisgiven +i
        for i in movingtowardsB[:(greatnesofMinimumofA)]:
            paisaisgiven = paisaisgiven +i
        j = greatnesofMinimumofA
        i = greatnessofminimumB
        
        for k in range(lessenessofminimumofB - greatnesofMinimumofA):
            if(movingtowardsA[i] < movingtowardsB[j]):
                paisaisgiven = paisaisgiven +movingtowardsA[i]
                i = i +1
            else:
                paisaisgiven = paisaisgiven +movingtowardsB[j]
                j = j +1


    print(paisaisgiven)