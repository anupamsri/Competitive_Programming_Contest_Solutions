S = str(input())
N = len(S)


def palindromic(word):
    if word == word[::-1]:
        return 1
    else:
        return 0


flag = palindromic(S)
flag2 = palindromic(S[0:(N - 1) // 2])
flag3 = palindromic(S[(N + 2) // 2:])
if(flag3 == 1 and flag == 1 and flag2 == 1):
    print('Yes')
else:
    print('No')