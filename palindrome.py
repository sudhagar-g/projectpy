text = input("enter the word : ").lower()
rev = ""


for char in text :
    rev = char + rev
if text == rev:
    print("This word is palindrome")
else:
    print("This word not palindrome")        




