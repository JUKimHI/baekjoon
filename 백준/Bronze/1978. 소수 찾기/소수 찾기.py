N = int(input())
l1 = list(map(int, input().split()))
l2 = []
for i in l1:
    count = 0
    if i == 2:
        l2.append(2)
    for j in range(2,i):
        if i % j == 0:
            count += 1
        if j == i-1 and count == 0:
            l2.append(i)
l2 = set(l2)
print(len(l2))