print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_pctg = float(input("How much tip percentage would you like to give? "))
people = float(input("How many people to split the bill? "))

total_tip = bill * (tip_pctg / 100)
total = total_tip + bill

print(f"Each person should pay: ${total/people}") 