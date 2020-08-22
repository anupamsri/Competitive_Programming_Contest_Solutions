N = int(input())
AC =[]
WA =[]
TLE =[]
RE =[]

for i in range(N):
    s = str(input())
    if s == "AC":
        AC.append(s)
    elif s == "WA":
        WA.append(s)
    elif s == "TLE":
        TLE.append(s)
    elif s =="RE":
        RE.append(s)
print("AC x "+str(len(AC)))
print("WA x "+str(len(WA)))
print("TLE x "+str(len(TLE)))
print("RE x "+str(len(RE)))
