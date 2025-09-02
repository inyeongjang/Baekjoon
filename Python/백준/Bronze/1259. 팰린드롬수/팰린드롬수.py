n_list = []

while True:
    n = input().strip()
    if n == "0":
        break
    n_list.append(n)

for n in n_list:
    if n == n[::-1]:
        print("yes")
    else:
        print("no")