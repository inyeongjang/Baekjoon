T = int(input())

for i in range(T): 
    R, S = input().split()
    P = ""
    for s in S:
        P += s * int(R)
    print(P)