# 1 

hour, minute = map(int, input().split())

if minute >= 45:
    minute -= 45
else:
    if hour != 0: 
        hour -= 1
    else: 
        hour = 23 
    minute += (60 - 45)

print(hour, minute)

# 2 

hour, minute = map(int, input().split())

minute -= 45 
if minute < 0:
    minute += 60 
    hour -= 1
    if hour < 0: 
        hour = 23

print(hour, minute)