# 1 

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

# 2 

N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
new_scores = [(s / M) * 100 for s in scores]
average = sum(new_scores) / N 

print(average)

# 3 

N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
average = sum(scores) / M * 100 / N 

print(average)