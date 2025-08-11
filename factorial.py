num  = int (input ("enter the number :"))
fact = 1

if num <= 1:
    print(num)
else:
    for i in range(1,num+1):
        fact *= i  
    print(fact)          


