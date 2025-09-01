# 1 

N, M = map(int, input().split())
cards = list(map(int, input().split()))

total = []

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total.append(cards[i] + cards[j] + cards[k])

total.sort(reverse=True)

for n in total:
    if n <= M:
        print(n)
        break

# 2

N, M = map(int, input().split())
cards = list(map(int, input().split()))

best = 0 
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k] 
            if total > best and total <= M:
                best = total 
                if best == M:
                    print(best)
                    exit()

print(best)