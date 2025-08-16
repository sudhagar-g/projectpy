try:
    num = int(input("enter the number: "))
    original = num
    rev = 0
    negative  = num < 0
    num  = abs(num)
    
    while num > 0:
        digits = num % 10
        rev = rev * 10 +digits
        num = num // 10
    print(rev)    

    if negative:
        rev = -rev

    if original == rev:
        print("this is palindrome number")
    else:
        print("this number not palindrome")        

except ValueError:
    print("please Enter number only")



           


