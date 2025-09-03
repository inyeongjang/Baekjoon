import string

S = input()

for ch in string.ascii_lowercase:
    print(S.find(ch), end=" ")