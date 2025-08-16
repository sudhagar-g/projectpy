word = str(input("enter the word : "))

container = {}

for char in word:
    if char in container:
        container[char] +=1
    else:
        container[char] =1  
print(container)       
        
       
