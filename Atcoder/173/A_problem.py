n = int(input())
count =0
while True:
    tmp = 1000*count
    if tmp>=n:
        break
    count+=1

print(1000*count-n)