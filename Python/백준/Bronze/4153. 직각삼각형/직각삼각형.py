while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    x, y, z = sorted([a, b, c])
    print("right" if x*x + y*y == z*z else "wrong")