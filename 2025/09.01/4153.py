# 1

a, b, c = map(int, input().split())

while (a+b+c!=0):
    a, b, c = sorted([a, b, c])
    if (a**2 + b**2) == c**2:
        print("right")
    else: 
        print("wrong")
    a, b, c = map(int, input().split())

# 2 

while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    x, y, z = sorted([a, b, c])
    print("right" if x*x + y*y == z*z else "wrong")