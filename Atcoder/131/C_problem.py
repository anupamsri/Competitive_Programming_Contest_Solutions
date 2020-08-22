A, B, C, D = map(int, input().split())


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a // gcd(a, b) * b


a = (A-1) - ((A-1) // C + (A-1) // D - (A-1) // lcm(C, D))
b = B - (B // C + B // D - B // lcm(C, D))
print(b-a)