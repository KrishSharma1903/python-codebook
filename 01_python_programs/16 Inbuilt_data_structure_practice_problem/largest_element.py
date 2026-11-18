def find_largest(numbers):
    max = numbers[0]
    for i in numbers:
        if i>max:
            max =i
    return max

print(find_largest([1,2,3,4,5])) 
