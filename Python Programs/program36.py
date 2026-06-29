import random 

alphabets = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*","("] 

no_alphabets = int(input("Enter the number of alphabets you want in your password: ")) 
no_numbers = int(input("Enter the number of numbers you want in your password: ")) 
no_special_char = int(input("Enter the number of special char you want in your password: ")) 

password_list = [ ] 

for char in range(0 ,no_alphabets): 
    password_list.append(random.choice(alphabets)) 


for char in range(0 ,no_numbers): 
        password_list.append(random.choice(numbers)) 


for char in range(0 ,no_special_char): 
            password_list.append(random.choice(special_characters)) 

# print(password_list) 
random.shuffle(password_list) 
 # print(password_list) 

password = "" 

for char in password_list: 
    password += char 

print(f"Your password is {password}")