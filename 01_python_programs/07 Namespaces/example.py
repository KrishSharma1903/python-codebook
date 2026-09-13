game_level = 3
enemy = ["Zombie" , "Skeleton" , "Aliens"]

def create_enemy():
    new_enemy = ""
    if game_level < 5: 
        new_enemy = enemy[0]
        print(new_enemy)


create_enemy()