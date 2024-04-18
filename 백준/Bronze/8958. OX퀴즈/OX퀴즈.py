T = int(input())
for _ in range(T):
    TF = input()
    score = 0
    sumscore = 0
    for i in TF:
        if i == 'O':
            score += 1
        else:
            score = 0
        sumscore += score
    print(sumscore)