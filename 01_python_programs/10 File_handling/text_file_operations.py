##File handling 
#file handling is a crucial part of any programming language. Python provides built-in functions and methods to read from and write to files, both text and binary. 

##read a whole file 
with open('example.txt','r') as file:
    content=file.read()
    print(content)

##Read a file line by line 
with open('example.txt','r') as file:
    for line in file:
        print(line.strip()) #s.strip removes the newline char 


##Writing in a file(overwriting)
with open('example.txt','w') as file:
    file.write("Hello World!\n")
    file.write("This is a new line \n")

##Writing in a file without overwriting 
with open('example.txt','a') as file:
    file.write("Append operation takes place")

### Writing a list of lines to a file
lines=['First line \n','Second line \n','Third line\n']
with open('example.txt','a') as file:
    file.writelines(lines)
     


