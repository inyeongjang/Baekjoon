# 1 

N = int(input())
num_list = list(map(int, input().split()))

count = N
for n in num_list:
    if n == 1:
        count -= 1
    for i in range(2, n):
        if n % i == 0:
            count -= 1 
            break 

print(count)

# 2

N = int(input())
num_list = list(map(int, input().split()))

cnt = 0
for n in num_list:
    if n < 2:
        continue 
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            break 
    else:
        cnt +=1

print(cnt)