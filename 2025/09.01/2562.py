# 1

num_list = [int(input()) for _ in range(9)]

max_index = 0
max_num = num_list[max_index]

for i in range(1, 9):
    if num_list[i]>max_num:
        max_num = num_list[i] 
        max_index = i

print(max_num)
print(max_index + 1)

# 2 

num_list = [int(input()) for _ in range(9)]

max_num = max(num_list)
max_index = num_list.index(max_num) + 1

print(max_num)
print(max_index)

# 3 

max_num = 0
max_index = 0

for i in range(1, 10):
    n = int(input())
    if n > max_num :
        max_num = n 
        max_index = i

print(max_num)
print(max_index)