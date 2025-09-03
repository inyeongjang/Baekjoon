N = int(input())

for n in range(N):
    S = input()
    score = 0
    sum = 0 
    for s in S:
        if s == "O":
            score += 1 
            sum += score 
        elif s == "X":
            score = 0
    print(sum)