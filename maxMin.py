num = [2,5,88,36,45,78,96,10,25,34,0,-1]
max_val = num[0]
min_val = num[0]

for i in num:
    if i > max_val:
        max_val = i

    elif i < min_val:
        min_val = i    

print(max_val)
print(min_val)          