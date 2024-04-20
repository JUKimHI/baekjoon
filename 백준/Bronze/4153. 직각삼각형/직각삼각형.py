while True:
    A,B,C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    if A == 0 and B == 0 and C == 0:
        break
    D = max(A, B, C)
    if D == A:
        if A**2 == B**2 + C**2:
            print('right')
        else:
            print('wrong')
    elif D == B:
        if B**2 == A**2 + C**2:
            print('right')
        else:
            print('wrong')
    else:
        if C**2 == A**2 + B**2:
            print('right')
        else:
            print('wrong')