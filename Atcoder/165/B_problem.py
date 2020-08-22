X = int(input())
year = 0
money = 100
while True:
    if money >= X:
        print(year)
        exit()
    money = int(money * 1.01)
    year+=1

