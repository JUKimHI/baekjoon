L = int(input())
S = input()
K = 0
for i in range(L):
    K += 31**i * (ord(S[i])-96)
print(K)