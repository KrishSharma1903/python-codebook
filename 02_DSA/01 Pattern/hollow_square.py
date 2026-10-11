def generate_hollow_square(n):
    square = []
    if n == 1:
        return ['*']
    square.append('*' * n)  # First row

    for _ in range(n - 2):
        square.append('*' + ' ' * (n - 2) + '*')
    
    square.append('*' * n)  # Last row
    
    # Return the list of rows
    return square

print(generate_hollow_square(5))