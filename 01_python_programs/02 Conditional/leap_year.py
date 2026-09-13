year = int(input("Enter the year: "))

if year% 4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(f"The {year} is a leap year")
        else:
            print(f"The {year} isn't a leap year.")
    else:
          print(f"The {year} is a leap year")
else:
    print(f"The {year} isn't a leap year.")