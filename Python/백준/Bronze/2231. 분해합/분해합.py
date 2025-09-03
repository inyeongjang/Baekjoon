N = int(input())

is_exist = 0 

for M in range(1, 1000001):
    total = M 
    temp = M
    while M != 0:
        total += M % 10
        M = M // 10 
    if total == N:
        print(temp)
        is_exist = 1 
        break;

if is_exist == 0:
    print(0)