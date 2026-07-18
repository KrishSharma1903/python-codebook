def calculate_distance(speed, time):
    distance = speed * time 
    return distance 
    
number_1 = int(input("Enter a number 1 "))
number_2 = int(input("Enter a number 2 "))

print(calculate_distance(number_1, number_2))