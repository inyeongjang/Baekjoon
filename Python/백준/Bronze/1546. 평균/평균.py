N = int(input())
scores = list(map(int, input().split()))

M = scores[0]
for i in range(1, N):
    if scores[i] > M:
        M = scores[i]

total = 0
for i in range(N):
    scores[i] = scores[i] / M * 100 
    total += scores[i]

average = total / N 
print(average)