T = int(input())
num_list = []

for i in range(T):
    a, b = map(int, input().split())
    num_list.append(a + b)

for n in num_list:
    print(n)