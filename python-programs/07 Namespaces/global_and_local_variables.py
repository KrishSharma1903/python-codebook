enimies = 1 # global

def increase_enimies():
    enimies = 2 #local
    print(f"Enemies inside the function are {enimies}")

# increase_enimies()
# print(f"Enemies outside the function are {enimies}")


player_health= 10

def drink_potion():
    potion_strength = 2
    print(player_health)


drink_potion()
print(player_health)