N = int(input())
l1 = []
for i in range(N):
    l1.append(input())

l2 = set(l1)
l2 = list(l2)
l2.sort()
l2.sort(key = len)

for j in l2:
    print(j)  