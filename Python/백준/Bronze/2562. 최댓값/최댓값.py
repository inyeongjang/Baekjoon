max_num = 0
max_index = 0

for i in range(1, 10):
    n = int(input())
    if n > max_num :
        max_num = n 
        max_index = i

print(max_num)
print(max_index)