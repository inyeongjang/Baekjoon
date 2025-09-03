import string

S = input()

for ch in string.ascii_lowercase:
    for i in range(len(S)):
        index = -1 
        if S[i] == ch:
            index = i
            break 
    print(index)