N = int(input()) 
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

shirt_bundles = sum((s + T - 1) // T for s in sizes)
pen_bundles, pen_singles = divmod(N, P)

print(shirt_bundles)
print(pen_bundles, pen_singles)