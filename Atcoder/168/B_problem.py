k = int(input())
S = str(input())
if(len(S)>k):
    print(S[:k]+'...')
else:
    print(S)