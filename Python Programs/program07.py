print("!!!!!!!!! Welcome to the tip calculator !!!!!!!!!")

bill = float(input("What is your bill? "))
tip= int(input("How much you want to tip? 10 12 15 "))
people = int(input("How many people are dividing the bill: "))

bill_after_tip = (tip/100)*bill + bill

bill_pp = round(bill_after_tip/people, 2)

print(bill_pp)