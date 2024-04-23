import sys
N = int(sys.stdin.readline())
l1 = [0] * 10001

for _ in range(N):
    l1[int(sys.stdin.readline())] += 1
    
for i in range(10001):
    if l1[i] != 0:
        for j in range(l1[i]):
            print(i)