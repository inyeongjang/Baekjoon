N = int(input())
scores = list(map(int, input().split()))

M = max(scores)
average = sum(scores) / M * 100 / N 

print(average)