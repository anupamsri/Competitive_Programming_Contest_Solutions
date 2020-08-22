S = str(input())
if S[-1] == '2' or S[-1]=='4' or S[-1] == '5'or S[-1]=='7' or S[-1]=='9':
    print('hon')
elif S[-1] == '0' or S[-1] == '1' or S[-1] == '6' or S[-1] == '8':
    print('pon')
else:
    print('bon')