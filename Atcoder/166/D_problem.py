X = int(input())
for A in range(-1000,1000):
    A5 = A**5
    for B in range(-1000,1000):
        if A5 - B**5 ==X:
            print(A,B)
            exit()
