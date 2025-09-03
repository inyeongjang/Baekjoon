n_list =[]

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break 
    n_list.append(a + b)

for n in n_list:
    print(n)