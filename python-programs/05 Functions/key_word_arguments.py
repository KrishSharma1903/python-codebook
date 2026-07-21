def print_examples(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} {value}")

print_examples(Name = "Krish" , Age = 21 ,  Country= "India")