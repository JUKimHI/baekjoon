S = list(input())
A = 'abcdefghijklmnopqrstuvwxyz'

for i in A:
    if i in S:
        print(S.index(i),end = ' ')
    if i not in S:
        print(-1,end = ' ')