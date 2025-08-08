# reversing interger
num = int(input("enter the number :")) #this line get input from  the user just  assume  number is (123456)
rev = 0                                 # now create variable with value 0  later store value 
negative = num < 0                      # check if the number is negative
num = abs(num)                          # work with absolute value

while num > 0:                  #loop run until  number come to 0 value
        digits = num % 10         # geting input number last digit  =>  123456 % 10 = 6
        rev = rev * 10 + digits    # sum like 0*10+ 6 => now rev store value 6
        num = num // 10             # 123456 // 10 => 12345  because // its a floor division its give whole number less then or equal to given(123456) number 
if negative:
    rev = -rev
print(rev)                          # printing the value



#3fdgsdf
