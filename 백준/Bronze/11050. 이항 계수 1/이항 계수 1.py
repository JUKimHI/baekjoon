N,K=map(int, input().split())
A=1
B=1
C=1
for i in range(1,N+1):
    A *= i
for j in range(1,N-K+1):
    B *= j
for k in range(1,K+1):
    C *= k
print(A//(B*C))