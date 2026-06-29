import random 

alphabets = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*","("] 

no_alphabets = int(input("Enter the number of alphabets you want in your password: ")) 
no_numbers = int(input("Enter the number of numbers you want in your password: ")) 
no_special_char = int(input("Enter the number of special char you want in your password: ")) 


password = ""

for _ in range(no_alphabets):
    password += random.choice(alphabets)

for _ in range(no_numbers):
    password += random.choice(numbers)

for _ in range(no_special_char):
    password += random.choice(special_characters)

print(f"Your password is: {password}")