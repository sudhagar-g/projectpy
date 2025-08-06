# reversing interger
num = int(input("enter the number :")) #this line get inpyt from user  assume  number as 123456
rev = 0 

while num > 0:                  #loop run until  number come to 0 value
        digits = num % 10         # geting input number last digit  =>  123456 % 10 = 6
        rev = rev * 10 + digits    # sum like 0*10+ 6 => now rev store value 6
        num = num // 10             # 123456 // 10 => 12345  because // its a floor division its give whole number less then or equal to given(123456) number 
print(rev)                          # printing the value



