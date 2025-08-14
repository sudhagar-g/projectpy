import random      

min_val = 0
max_val =  100
random_number = random.randint(min_val,max_val)

attempt = 0
chance = 10

while attempt < chance:
    try :
        my_guess = int(input("enter the number between 0 and 100 : ") )
        attempt +=1

        if  my_guess < min_val or my_guess > max_val:
            print(f"please enter the number between {min_val} and {max_val}")
        elif my_guess < random_number:
            print("Too low ")
        elif my_guess > random_number:
            print("Too Hihg")
        else:
            print(f"congratulation you won the game and the number was {random_number} and guess the number in {attempt}th attempt")
            break
    except ValueError :
        print("  please enter the number") 
         
else:
    print(f"sorry you lost the  all chance the number was {random_number}")                      
                 





