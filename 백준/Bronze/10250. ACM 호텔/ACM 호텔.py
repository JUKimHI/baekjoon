T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    
    floor = N%H
    room = (N//H) + 1
    
    if N%H == 0:
        floor = H
        room -= 1
    if room < 10:
        print(floor,'0',room,sep='')
    else:
        print(floor,room,sep='')