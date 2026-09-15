def generate_diamond(n):
    lst =[]
    if 1 <= n <= 100:
        for i in range(1,n+1):
            spaces = " " * (n - i)
            stars = "*" * (2 * i - 1)
            lst.append(spaces + stars + spaces)
        
        for j in range(2, n + 1):
                stars = '*' * (2 * (n - j + 1) - 1)
                spaces = ' ' * (j - 1)
                lst.append(spaces + stars + spaces)    
        return lst

print(generate_diamond(3))


def generate_diamond(n):
 
    diamond = []
    
   
    for i in range(1, n + 1):
         stars = '*' * (2 * i - 1)
         spaces = ' ' * (n - i)
         diamond.append(spaces + stars + spaces)
    
   
    for i in range(n - 1, 0, -1):
       stars = '*' * (2 * i - 1)
       spaces = ' ' * (n - i)
       diamond.append(spaces + stars + spaces)
    
    return diamond
print(generate_diamond(3))