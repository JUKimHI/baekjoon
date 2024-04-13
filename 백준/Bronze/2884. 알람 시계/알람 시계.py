H,M = map(int, input().split())
if H==0:
    if M>=45:
        print(H,M-45)
    elif M<45:
        M = M+60
        print(23,M-45)
if H>0:
    if M>=45:
        print(H,M-45)
    elif M<45:
        M=M+60
        print(H-1,M-45)