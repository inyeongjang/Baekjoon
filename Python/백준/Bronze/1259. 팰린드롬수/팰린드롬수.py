n_list = []

while True:
    n = int(input())
    if n == 0:
        break
    n_list.append(n)

for n in n_list: 
    number = []
    while (n != 0):
        number.append(n % 10)
        n = n // 10
    
    a = 0
    b = len(number) - 1
    is_same = 1

    while (a < b):
        if (number[a] != number[b]):
            is_same = 0
            break
        a += 1
        b -= 1 

    if is_same == 1:
        print("yes") 
    else:
        print("no")