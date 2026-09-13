def calc_lift_rounds(n , capacity):
    rounds = 0
    
    while n > 0:
        n -= capacity
        rounds += 1

    return rounds


print(calc_lift_rounds(10,3))