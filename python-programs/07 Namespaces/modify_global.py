enimies = 1 # global

def increase_enimies(enemy):
    # global enimies 
    # enimies +=1 not optimal as it may cause a problem in the future else we can
    print(f"Enemies inside the function are {enimies}")
    return enimies + 1

enimies = increase_enimies(enimies)
print(f"Enemies outside the function are {enimies}")
