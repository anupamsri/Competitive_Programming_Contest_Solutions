
N = int(input())
def divisor(n):
    fac = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            fac.append(i)
            if i * i != n:
                fac.append(n // i)
    return sorted(fac)
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
L = divisor(N)
count = 0
for i in L[1::]:
    if len(factorization(i))==1:
        if N % i == 0:
            N = N/i
            count+=1
print(count)