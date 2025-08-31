# 1 

N = int(input()) 
S, M, L, XL, XXL, XXXL = map(int, input().split())
T, P = map(int, input().split())

size = [S, M, L, XL, XXL, XXXL] 
shirts = 0
pen = 0

for i in size:
    if (i % T > 0):
        count = i // T + 1 
    else:
        count = i // T
    shirts += count 
    pen += i 

print(shirts)
print(pen // P, pen % P)

# 2 

N = int(input()) 
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_bundles = sum((s + T - 1) // T for s in sizes)
pen_bundles, pen_singles = divmod(N, P)

print(shirt_bundles)
print(pen_bundles, pen_singles)