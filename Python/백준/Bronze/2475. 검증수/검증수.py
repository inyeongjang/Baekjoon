numbers = list(map(int, input().split())) 

sum = 0 

for n in numbers: 
    sum += n**2 

print(sum % 10)